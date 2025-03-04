n = int(input())
next_closest_99 = n - (n % 100) + 99
if next_closest_99 < n:
    print(next_closest_99)
else:
    print(next_closest_99 - 99)