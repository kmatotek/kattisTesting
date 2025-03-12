# Reading input values
nums = list(map(int, input().split()))
letts = input()

# Sorting the numbers based on the order given by letts
sorted_nums = sorted(nums, key=lambda x: letts.index(str(x)))

# Printing the sorted numbers
print(' '.join(map(str, sorted_nums)))