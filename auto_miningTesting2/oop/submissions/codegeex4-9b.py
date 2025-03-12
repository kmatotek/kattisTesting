def count_matching_words(words, patterns):
    # Create a dictionary to store the frequency of each word
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # Process each pattern and count the matching words
    results = []
    for pattern in patterns:
        count = 0
        # Check each word in the dictionary
        for word in word_count:
            if is_match(word, pattern):
                count += word_count[word]
        results.append(count)
    
    return results

def is_match(word, pattern):
    # If pattern is longer than word, it cannot match
    if len(pattern) > len(word):
        return False
    
    # Check if each character in the pattern matches the corresponding character in the word
    for i in range(len(pattern)):
        if pattern[i] != '*' and pattern[i] != word[i]:
            return False
    return True

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse the first line to get N and Q
index = 0
N = int(data[index])
Q = int(data[index + 1])
index += 2

# Parse the next N lines to get the words
words = []
for _ in range(N):
    words.append(data[index])
    index += 1

# Parse the next Q lines to get the patterns
patterns = []
for _ in range(Q):
    patterns.append(data[index])
    index += 1

# Get the results for each pattern
results = count_matching_words(words, patterns)

# Print the results
for result in results:
    print(result)