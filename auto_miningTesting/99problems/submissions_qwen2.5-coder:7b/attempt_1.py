# Read input from standard input
N = int(input())

# Calculate the nearest number ending in 99
if N % 100 == 99:
    closest_number = N
elif N % 100 <= 50:
    closest_number = N - (N % 100)
else:
    closest_number = N + (100 - N % 100)

# Print the result
print(closest_number)