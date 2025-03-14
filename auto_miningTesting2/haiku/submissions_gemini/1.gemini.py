def is_valid_haiku(syllable_count, first_phrase_syllables, second_phrase_syllables, third_phrase_syllables):
    """
    Checks if the given phrases form a haiku based on the syllable counts.

    Args:
        syllable_count: The total number of syllables.
        first_phrase_syllables: A list of integers representing syllable counts for each word in the first phrase.
        second_phrase_syllables: A list of integers representing syllable counts for each word in the second phrase.
        third_phrase_syllables: A list of integers representing syllable counts for each word in the third phrase.

    Returns:
        True if the phrases form a haiku, False otherwise.
    """
    return sum(first_phrase_syllables) == 5 and sum(second_phrase_syllables) == 7 and sum(
        third_phrase_syllables) == 5


def count_phrase_syllables(phrase_words, available_syllables):
    """
    Counts the syllables in a phrase, attempting to match words to available syllables.

    Args:
        phrase_words: A list of words in the phrase.
        available_syllables: A list of available syllables.

    Returns:
        A list of syllable counts for each word in the phrase if a match is found, otherwise None.
    """
    phrase_syllables = []
    current_syllable_index = 0
    for word in phrase_words:
        word_syllables = []
        current_word_index = 0
        while current_word_index < len(word):
            if current_syllable_index >= len(available_syllables):
                return None  # Not enough syllables
            current_syllable = available_syllables[current_syllable_index]
            if word[current_word_index:].startswith(current_syllable):
                word_syllables.append(len(current_syllable))
                current_word_index += len(current_syllable)
                current_syllable_index += 1
            else:
                return None  # Syllable mismatch
        phrase_syllables.append(len(word_syllables))
    return phrase_syllables


def main():
    """
    Main function to process input and determine if the poem is a haiku.
    """
    total_syllables = int(input())
    available_syllables = input().split()
    first_phrase_words = input().split()
    second_phrase_words = input().split()
    third_phrase_words = input().split()

    first_phrase_syllables = count_phrase_syllables(first_phrase_words, available_syllables)
    second_phrase_syllables = count_phrase_syllables(second_phrase_words, available_syllables)
    third_phrase_syllables = count_phrase_syllables(third_phrase_words, available_syllables)

    if first_phrase_syllables and second_phrase_syllables and third_phrase_syllables and is_valid_haiku(
            total_syllables, first_phrase_syllables, second_phrase_syllables, third_phrase_syllables):
        print("haiku")
    else:
        print("come back next year")


if __name__ == "__main__":
    main()