def nearest_ending_in_99(n):
    if n % 100 >= 50:   # If last two digits are between 50-99 inclusive, round it up to next multiple of 100.
        return (n + 99) - (n % 100)
    else:                 # Else round down to the nearest multiple of 100.
        return n - (n % 100)

# Read input from standard input using input() function.
N = int(input())
print(nearest_ending_in_99(N))