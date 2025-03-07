#!/usr/bin/env python
from __future__ import print_function
import argparse
import os
import re
import sys
import time

import requests
import requests.exceptions

from lxml.html import fragment_fromstring

# Python 2/3 compatibility
if sys.version_info[0] >= 3:
    import configparser
else:
    import ConfigParser as configparser

_DEFAULT_CONFIG = '/usr/local/etc/kattisrc'
_LANGUAGE_GUESS = {
    '.c': 'C',
    '.c++': 'C++',
    '.cc': 'C++',
    '.c#': 'C#',
    '.cpp': 'C++',
    '.cs': 'C#',
    '.cxx': 'C++',
    '.cbl': 'COBOL',
    '.cob': 'COBOL',
    '.cpy': 'COBOL',
    '.fs': 'F#',
    '.go': 'Go',
    '.hs': 'Haskell',
    '.java': 'Java',
    '.js': 'JavaScript (Node.js)',
    '.ts': 'TypeScript',
    '.kt': 'Kotlin',
    '.lisp': 'Common Lisp',
    '.cl': 'Common Lisp',
    '.m': 'Objective-C',
    '.ml': 'OCaml',
    '.pas': 'Pascal',
    '.php': 'PHP',
    '.pl': 'Prolog',
    '.py': 'Python 3',
    '.pyc': 'Python 3',
    '.rb': 'Ruby',
    '.rs': 'Rust',
    '.scala': 'Scala',
    '.f90': 'Fortran',
    '.f': 'Fortran',
    '.for': 'Fortran',
    '.sh': 'Bash',
    '.apl': 'APL',
    '.ss': 'Gerbil',
    '.jl': 'Julia',
    '.vb': 'Visual Basic',
    '.dart': 'Dart',
    '.zig': 'Zig',
    '.swift': 'Swift',
    '.nim': 'Nim',
}
_GUESS_MAINCLASS = {'Java', 'Kotlin', 'Scala'}
_GUESS_MAINFILE = {'APL', 'Bash', 'Dart', 'Gerbil', 'JavaScript (Node.js)', 'Julia',
                   'Common Lisp', 'Pascal', 'PHP', 'Python 2', 'Python 3', 'Ruby',
                   'Rust', 'TypeScript', 'Zig'}

_HEADERS = {'User-Agent': 'kattis-cli-submit'}

_RUNNING_STATUS = 5
_COMPILE_ERROR_STATUS = 8
_ACCEPTED_STATUS = 16
_STATUS_MAP = {
    0: 'New',
    1: 'New',
    2: 'Waiting for compile',
    3: 'Compiling',
    4: 'Waiting for run',
    _RUNNING_STATUS: 'Running',
    6: 'Judge Error',
    7: 'Submission Error',
    _COMPILE_ERROR_STATUS: 'Compile Error',
    9: 'Run Time Error',
    10: 'Memory Limit Exceeded',
    11: 'Output Limit Exceeded',
    12: 'Time Limit Exceeded',
    13: 'Illegal Function',
    14: 'Wrong Answer',
    _ACCEPTED_STATUS: 'Accepted',
}


class ConfigError(Exception):
    pass


def get_url(cfg, option, default):
    if cfg.has_option('kattis', option):
        return cfg.get('kattis', option)
    else:
        return 'https://%s/%s' % (cfg.get('kattis', 'hostname'), default)


def get_config():
    cfg = configparser.ConfigParser()
    if os.path.exists(_DEFAULT_CONFIG):
        cfg.read(_DEFAULT_CONFIG)

    if not cfg.read([os.path.join(os.path.expanduser("~"), '.kattisrc'),
                     os.path.join(os.path.dirname(sys.argv[0]), '.kattisrc')]):
        raise ConfigError('''\
I failed to read in a config file from your home directory or from the
same directory as this script. To download a .kattisrc file please visit
https://<kattis>/download/kattisrc

The file should look something like this:
[user]
username: yourusername
token: *********

[kattis]
hostname: <kattis>
loginurl: https://<kattis>/login
submissionurl: https://<kattis>/submit
submissionsurl: https://<kattis>/submissions''')
    return cfg


def is_python2(files):
    python2 = re.compile(r'^\s*\bprint\b *[^ \(\),\]]|\braw_input\b')
    for filename in files:
        try:
            with open(filename) as f:
                for index, line in enumerate(f):
                    if index == 0 and line.startswith('#!'):
                        if 'python2' in line:
                            return True
                        if 'python3' in line:
                            return False
                    if python2.search(line.split('#')[0]):
                        return True
        except IOError:
            return False
    return False


def guess_language(ext, files):
    if ext == ".C":
        return "C++"
    ext = ext.lower()
    if ext == ".h":
        if any(f.endswith(".c") for f in files):
            return "C"
        else:
            return "C++"
    if ext == ".py":
        if is_python2(files):
            return "Python 2"
        else:
            return "Python 3"
    return _LANGUAGE_GUESS.get(ext, None)


def guess_mainfile(language, files):
    for filename in files:
        if os.path.splitext(os.path.basename(filename))[0] in ['main', 'Main']:
            return filename
    for filename in files:
        try:
            with open(filename) as f:
                conts = f.read()
                if language in ['Java', 'Rust', 'Scala', 'Kotlin'] and re.search(r' main\s*\(', conts):
                    return filename
                if language == 'Pascal' and re.match(r'^\s*[Pp]rogram\b', conts):
                    return filename
        except IOError:
            pass
    return files[0]


def guess_mainclass(language, files):
    if language in _GUESS_MAINFILE and len(files) > 1:
        return os.path.basename(guess_mainfile(language, files))
    if language in _GUESS_MAINCLASS:
        mainfile = os.path.basename(guess_mainfile(language, files))
        name = os.path.splitext(mainfile)[0]
        if language == 'Kotlin':
            return name[0].upper() + name[1:] + 'Kt'
        return name
    return None


# Use a session for persistent connection/cookies.
def login(session, login_url, username, password=None, token=None):
    login_args = {'user': username, 'script': 'true'}
    if password:
        login_args['password'] = password
    if token:
        login_args['token'] = token
    return session.post(login_url, data=login_args)


def login_from_config(session, cfg):
    username = cfg.get('user', 'username')
    password = token = None
    try:
        password = cfg.get('user', 'password')
    except configparser.NoOptionError:
        pass
    try:
        token = cfg.get('user', 'token')
    except configparser.NoOptionError:
        pass
    if password is None and token is None:
        raise ConfigError('''\
Your .kattisrc file appears corrupted. It must provide a token (or a
KATTIS password).

Please download a new .kattisrc file''')
    loginurl = get_url(cfg, 'loginurl', 'login')
    return login(session, loginurl, username, password, token)


def submit(session, submit_url, problem, language, files, mainclass='', tag='', assignment=None, contest=None):
    data = {'submit': 'true',
            'submit_ctr': 2,
            'language': language,
            'mainclass': mainclass,
            'problem': problem,
            'tag': tag,
            'script': 'true'}

    if assignment is not None:
        data['assignment'] = assignment
    if contest is not None:
        data['contest'] = contest
    sub_files = []
    for f in files:
        with open(f, 'rb') as sub_file:
            sub_files.append(('sub_file[]',
                              (os.path.basename(f),
                               sub_file.read(),
                               'application/octet-stream')))
    return session.post(submit_url, data=data, files=sub_files)


def get_submission_status(session, submission_url):
    reply = session.get(submission_url + '?json')
    return reply.json()


_RED_COLOR = 31
_GREEN_COLOR = 32
def color(s, c):
    return '\x1b[%sm%s\x1b[0m' % (c, s)


def show_judgement(session, submission_url, cfg):
    print()
    while True:
        status = get_submission_status(session, submission_url)
        status_id = status['status_id']
        testcases_done = status['testcase_index']
        testcases_total = status['row_html'].count('<i') - 1

        status_text = _STATUS_MAP.get(status_id, 'Unknown status %s' % status_id)

        if status_id < _RUNNING_STATUS:
            print('\r%s...' % (status_text), end='')
        else:
            print('\rTest cases: ', end='')

        if status_id == _COMPILE_ERROR_STATUS:
            print('\r%s' % color(status_text, _RED_COLOR), end='')
            try:
                root = fragment_fromstring(status['feedback_html'], create_parent=True)
                error = root.find('.//pre').text
                print(color(':', _RED_COLOR))
                print(error, end='')
            except:
                pass
        elif status_id < _RUNNING_STATUS:
            print('\r%s...' % (status_text), end='')
        else:
            print('\rTest cases: ', end='')
            if testcases_total == 0:
                print('???', end='')
            else:
                s = '.' * (testcases_done - 1)
                if status_id == _RUNNING_STATUS:
                    s += '?'
                elif status_id == _ACCEPTED_STATUS:
                    s += '.'
                else:
                    s += 'x'
                print('[%-*s]  %d / %d' % (testcases_total, s, testcases_done, testcases_total), end='')

        sys.stdout.flush()

        if status_id > _RUNNING_STATUS:
            print()
            success = status_id == _ACCEPTED_STATUS
            try:
                root = fragment_fromstring(status['row_html'], create_parent=True)
                cpu_time = root.find('.//*[@data-type="cpu"]').text
                status_text += " (" + cpu_time + ")"
            except:
                pass
            if status_id != _COMPILE_ERROR_STATUS:
                print(color(status_text, _GREEN_COLOR if success else _RED_COLOR))
            return success

        time.sleep(0.25)


def confirm_or_die(problem, language, files, mainclass, tag):
    print('Problem:', problem)
    print('Language:', language)
    print('Files:', ', '.join(files))
    if mainclass:
        if language in _GUESS_MAINFILE:
            print('Main file:', mainclass)
        else:
            print('Mainclass:', mainclass)
    if tag:
        print('Tag:', tag)
    print('Submit (y/N)?')
    if sys.stdin.readline().upper()[:-1] != 'Y':
        print('Cancelling')
        sys.exit(1)


def get_submission_url(submit_response, cfg):
    m = re.search(r'Submission ID: (\d+)', submit_response)
    if m:
        submissions_url = get_url(cfg, 'submissionsurl', 'submissions')
        submission_id = m.group(1)
        return '%s/%s' % (submissions_url, submission_id)


def main():
    parser = argparse.ArgumentParser(prog='kattis', description='Submit a solution to Kattis')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--assignment',
                        help='Short name of assignment you want to submit to\nOverrides default guess (server guesses based on assignments you are in)')
    group.add_argument('-c', '--contest',
                        help='Short name of contest you want to submit to\nOverrides default guess (server guesses based on contests you are in)')
    parser.add_argument('-p', '--problem',
                        help='Which problem to submit to.\nOverrides default guess (first part of first filename)')
    parser.add_argument('-m', '--mainclass',
                        help='Sets mainclass.\nOverrides default guess (first part of first filename)')
    parser.add_argument('-l', '--language',
                        help='Sets language.\nOverrides default guess (based on suffix of first filename)')
    parser.add_argument('-t', '--tag',
                        help=argparse.SUPPRESS)
    parser.add_argument('-f', '--force',
                        help='Force, no confirmation prompt before submission',
                        action='store_true')
    parser.add_argument('files', nargs='+')

    args = parser.parse_args()
    files = args.files

    try:
        cfg = get_config()
    except ConfigError as exc:
        print(exc)
        sys.exit(1)

    problem, ext = os.path.splitext(os.path.basename(files[0]))
    language = guess_language(ext, files)
    mainclass = guess_mainclass(language, files)
    tag = args.tag

    problem = problem.lower()

    if args.problem:
        problem = args.problem

    if args.mainclass is not None:
        mainclass = args.mainclass

    if args.language:
        language = args.language

    if language is None:
        print('No language specified, and I failed to guess language from filename extension "%s"' % (ext,))
        sys.exit(1)

    files = sorted(list(set(args.files)))

    # Create a persistent session with custom headers.
    session = requests.Session()
    session.headers.update(_HEADERS)

    try:
        login_reply = login_from_config(session, cfg)
    except ConfigError as exc:
        print(exc)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print('Login connection failed:', err)
        sys.exit(1)

    if login_reply.status_code != 200:
        print('Login failed.')
        if login_reply.status_code == 403:
            print('Incorrect username or password/token (403)')
        elif login_reply.status_code == 404:
            print('Incorrect login URL (404)')
        else:
            print('Status code:', login_reply.status_code)
        sys.exit(1)

    submit_url = get_url(cfg, 'submissionurl', 'submit')

    if not args.force:
        confirm_or_die(problem, language, files, mainclass, tag)

    try:
        result = submit(session, submit_url, problem, language, files, mainclass, tag,
                        args.assignment, args.contest)
    except requests.exceptions.RequestException as err:
        print('Submit connection failed:', err)
        sys.exit(1)

    if result.status_code != 200:
        print('Submission failed.')
        if result.status_code == 403:
            print('Access denied (403)')
        elif result.status_code == 404:
            print('Incorrect submit URL (404)')
        else:
            print('Status code:', result.status_code)
        sys.exit(1)

    plain_result = result.content.decode('utf-8').replace('<br />', '\n')
    print(plain_result)

    submission_url = None
    try:
        submission_url = get_submission_url(plain_result, cfg)
    except configparser.NoOptionError:
        pass

    if submission_url:
        print(submission_url)
        if not show_judgement(session, submission_url, cfg):
            sys.exit(1)


if __name__ == '__main__':
    main()
