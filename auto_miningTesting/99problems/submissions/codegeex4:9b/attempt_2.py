def closest_price_ending_in_99(N):
    lower_bound = (N // 100) * 100
    upper_bound = lower_bound + 100
    lower_closest = lower_bound + 99
    upper_closest = upper_bound - 1

    if N - lower_closest <= upper_closest - N:
        return lower_closest
    else:
        return upper_closest

# Reading input from standard input
N = int(input().strip())

# Finding the closest price ending in 99
result = closest_price_ending_in_99(N)

# Writing output to standard output
print(result)