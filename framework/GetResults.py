import os
import re
import argparse

# Remove ANSI escape codes and get the last non-empty line.
def get_last_non_empty_line(text):
    clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    lines = clean_text.splitlines()
    for line in reversed(lines):
        if line.strip():
            return line.strip()
    return ""

# Extract passed and total test cases from feedback.
def get_test_cases_info(feedback):
    matches = re.findall(r"Test cases:\s*\[.*?\]\s*(\d+)\s*/\s*(\d+)", feedback)
    if matches:
        last_match = matches[-1]
        passed = int(last_match[0])
        total = int(last_match[1])
        return passed, total  # Adjust passed count if needed.
    return 0, 0

# Extract Python code from a message (if needed).
def get_python(message):
    start_code_block = message.find("```Python")
    if start_code_block == -1:
        start_code_block = message.find("```python")
    if start_code_block == -1:
        start_code_block = message.find("```")
        cut_string = message[start_code_block + 3:]
    else:
        cut_string = message[start_code_block + 10:]
    end_code_block = cut_string.find("```")
    return cut_string[:end_code_block].strip()

# Process a single problem folder for a given model.
def process_problem_folder(folder_path, model, attempts=3):
    submissions_folder = os.path.join(folder_path, f"submissions_{model}")
    results_folder = os.path.join(folder_path, f"results_{model}")
    
    attempt_data = {}
    for attempt in range(1, attempts + 1):
        result_file = os.path.join(results_folder, f"attempt_{attempt}_result.txt")
        submission_file = os.path.join(submissions_folder, f"attempt_{attempt}.py")
        
        # If neither result nor submission file exists, assume no further attempts exist.
        if not os.path.exists(result_file) and not os.path.exists(submission_file):
            break
        
        data = {"status": None, "passed": 0, "total": 0, "code": "", "error_message": ""}
        
        if os.path.exists(result_file):
            with open(result_file, "r", encoding="utf-8") as f:
                result_content = f.read()
            data["status"] = get_last_non_empty_line(result_content)
            passed, total = get_test_cases_info(result_content)
            data["passed"] = passed
            data["total"] = total
            data["error_message"] = get_last_non_empty_line(result_content)
        else:
            print(f"Result file for attempt {attempt} in {folder_path} does not exist.")
        
        if os.path.exists(submission_file):
            with open(submission_file, "r", encoding="utf-8") as f:
                data["code"] = f.read()
        else:
            print(f"Submission file for attempt {attempt} in {folder_path} does not exist.")
        
        attempt_data[attempt] = data
        
        # If the solution is accepted, skip checking further attempts.
        if data["status"] == "Accepted":
            break
    
    # Determine if the problem "passed with prompting":
    passed_with_prompting = (
        attempt_data.get(1, {}).get("status") != "Accepted" and
        (attempt_data.get(2, {}).get("status") == "Accepted" or 
         attempt_data.get(3, {}).get("status") == "Accepted")
    )
    
    # Choose best attempt: earliest accepted if available; otherwise, the one with the most passed tests.
    accepted_attempts = {a: d for a, d in attempt_data.items() if d["status"] == "Accepted"}
    if accepted_attempts:
        best_attempt = min(accepted_attempts.keys())
    else:
        if attempt_data:
            best_attempt = max(attempt_data.items(), key=lambda item: item[1]["passed"])[0]
        else:
            best_attempt = None
    
    return attempt_data, passed_with_prompting, best_attempt


def main():
    parser = argparse.ArgumentParser(description="Analyze autoprompting submission results.")
    parser.add_argument("--dir", default="./auto_miningTesting",
                        help="Base directory containing problem folders")
    parser.add_argument("--model", default="llama3",
                        help="Model name used in directory naming (e.g., submissions_<model>)")
    parser.add_argument("--attempts", type=int, default=3,
                        help="Number of attempts per problem to process")
    args = parser.parse_args()

    base_dir = args.dir
    model = args.model
    attempts = args.attempts

    # Iterate over each problem folder in the base directory.
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue

        print(f"\nProcessing problem folder: {folder_name}")
        attempt_data, passed_with_prompting, best_attempt = process_problem_folder(folder_path, model, attempts)

        print("Summary of Attempts:")
        for attempt in range(1, attempts + 1):
            data = attempt_data.get(attempt, {})
            print(f"Attempt {attempt}:")
            print(f"  Status: {data.get('status')}")
            print(f"  Passed Test Cases: {data.get('passed')} / {data.get('total')}")
            if data.get('status') != "Accepted":
                print(f"  Error Message: {data.get('error_message')}")
        print(f"Passed with prompting: {passed_with_prompting}")
        print(f"Best attempt (data to report): Attempt {best_attempt}")
        print("-" * 40)

if __name__ == "__main__":
    main()
