# Read input from standard input
N = int(input())

# Calculate the nearest number ending in 99
if N % 100 == 99:
    closest_number = N
elif N % 100 <= 50:
    closest_number = N - (N % 100)
else:
    closest_number = N + (100 - N % 100)

# Ensure the result ends in 99 if it's exactly halfway between two multiples of 100
if N % 100 == 50:
    closest_number += 50

# Print the result
print(closest_number)