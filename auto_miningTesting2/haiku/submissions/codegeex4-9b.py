def is_haiku(syllables, poem):
    syllable_count = {'five': 0, 'seven': 0, 'five_again': 0}
    required_syllable_counts = {'five': 5, 'seven': 7, 'five_again': 5}

    def count_syllables(word):
        word_syllable_count = 0
        vowels = "aeiouy"
        if len(word) == 1 and word not in vowels:
            word_syllable_count += 1
        else:
            word_syllable_count += sum(1 for char in word[1:] if char in vowels)
            if word[0] in vowels:
                word_syllable_count += 1
        return word_syllable_count

    def is_valid_haiku():
        return (syllable_count['five'] == required_syllable_counts['five'] and
                syllable_count['seven'] == required_syllable_counts['seven'] and
                syllable_count['five_again'] == required_syllable_counts['five_again'])

    current_phrase = []
    for word in syllables:
        current_phrase.append(word)
        syllable_count_for_word = count_syllables(word)
        if len(current_phrase) == 1:
            syllable_count['seven'] += syllable_count_for_word
        elif len(current_phrase) == 2:
            syllable_count['five'] += syllable_count_for_word
        else:
            syllable_count['five_again'] += syllable_count_for_word

        if is_valid_haiku():
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    syllables = data[1:n+1]
    poem_lines = data[n+1:n+4]

    poem = []
    for line in poem_lines:
        poem.extend(line.split())

    if is_haiku(syllables, poem):
        print("haiku")
    else:
        print("come back next year")

if __name__ == "__main__":
    main()