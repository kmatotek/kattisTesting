def count_covered_words(words, patterns):
    result = []
    
    for pattern in patterns:
        count = 0
        
        # Check each word to see if it covers the pattern
        for word in words:
            len_word = len(word)
            len_pattern = len(pattern)
            
            # Iterate through all possible positions of the wildcard '*'
            for i in range(len_word - len_pattern + 1):
                match = True
                for j in range(len_pattern):
                    if pattern[j] != '*' and (i + j >= len_word or word[i + j] != pattern[j]):
                        match = False
                        break
                if match:
                    count += 1
                    break
        
        result.append(count)
    
    return result

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])

words = data[2:N + 2]
patterns = data[N + 2:]

# Compute the results
results = count_covered_words(words, patterns)

# Print the results
for result in results:
    print(result)