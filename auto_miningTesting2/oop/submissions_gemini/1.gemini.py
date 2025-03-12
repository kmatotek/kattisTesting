def count_matching_phrases(phrase_collection, search_term):
    """
    Counts how many phrases in the collection match the given search term,
    where '*' in the search term can match any sequence of characters.

    Args:
      phrase_collection: A list of phrases (strings).
      search_term: A string representing the search pattern, possibly containing '*'.

    Returns:
      The number of phrases matching the search term.
    """

    matching_count = 0
    for phrase in phrase_collection:
        if match_pattern(phrase, search_term):
            matching_count += 1
    return matching_count

def match_pattern(phrase, search_term):
    """
    Checks if a phrase matches a given search term,
    where '*' in the search term can match any sequence of characters.

    Args:
      phrase: The phrase (string) to check.
      search_term: The search pattern (string) potentially containing '*'.

    Returns:
      True if the phrase matches the pattern, False otherwise.
    """

    if '*' not in search_term:
        return phrase == search_term
    
    parts = search_term.split('*')
    if not phrase.startswith(parts[0]):
        return False

    for i in range(1, len(parts)):
        if parts[i] and not parts[i] in phrase:
            return False
    
    return True


def main():
    """
    Reads input, processes queries, and prints the results.
    """

    num_phrases, num_queries = map(int, input().split())
    phrases = []
    for _ in range(num_phrases):
        phrases.append(input())

    for _ in range(num_queries):
        search_term = input()
        matching_count = count_matching_phrases(phrases, search_term)
        print(matching_count)

if __name__ == "__main__":
    main()