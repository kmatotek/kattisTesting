def longest_subarray_with_exactly_two_occurrences(arr):
    from collections import Counter
    count = Counter(arr)
    max_length = 0
    for num in count:
        if count[num] == 2:
            max_length = max(max_length, 2)
    return max_length

# Reading input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Finding the result
result = longest_subarray_with_exactly_two_occurrences(arr)

# Printing the result
print(result)