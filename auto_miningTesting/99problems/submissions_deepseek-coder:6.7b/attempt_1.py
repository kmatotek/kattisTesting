def closest_ending_in_99(n):
    if n % 100 >= 50:
        return (n // 100 + 1) * 100
    else:
        return n - n % 100

# read the input number
n = int(input())
print(closest_ending_in_99(n))