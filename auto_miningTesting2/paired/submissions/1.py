def find_longest_subarray(n, arr):
    longest_subarray_len = 0
    subarray_start = 0
    last_index = dict()
    for current_index in range(n):
        if arr[current_index] in last_index:
            subarray_start = max(subarray_start, last_index[arr[current_index]] + 1)
        longest_subarray_len = max(longest_subarray_len, current_index - subarray_start + 1)
        last_index[arr[current_index]] = current_index
    return longest_subarray_len

n = int(input().strip())
arr = list(map(int, input().split()))

print(find_longest_subarray(n, arr))