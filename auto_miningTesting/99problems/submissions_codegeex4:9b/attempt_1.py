def nearest_multiple_of_99(n):
    lower = (n // 100) * 100
    upper = lower + 100
    if abs(n - lower) <= abs(upper - n):
        return lower + 99
    else:
        return upper + 99

# Read input from standard input
n = int(input().strip())

# Get the nearest multiple of 99
result = nearest_multiple_of_99(n)

# Print the result to standard output
print(result)