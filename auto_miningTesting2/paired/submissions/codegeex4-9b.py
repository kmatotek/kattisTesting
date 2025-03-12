def longest_subarray_with_exactly_two_occurrences(arr):
    from collections import defaultdict
    
    count_map = defaultdict(int)
    max_length = 0
    
    start = 0
    for end in range(len(arr)):
        count_map[arr[end]] += 1
        
        while count_map[arr[end]] > 2:
            count_map[arr[start]] -= 1
            start += 1
        
        if count_map[arr[end]] == 2:
            max_length = max(max_length, end - start + 1)
    
    return max_length

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:n+1]))

# Finding the result
result = longest_subarray_with_exactly_two_occurrences(arr)

# Printing the result
print(result)