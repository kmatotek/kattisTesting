from math import ceil, floor

N = int(input())

# find the nearest number to N that is divisible by 100 and ends in 99
closest_number = (ceil(N / 100) * 100 - 99) if (ceil(N / 100) * 100 - 99) % 10 == 0 else (floor(N / 100 + 1) * 100 - 99)

print(closest_number)