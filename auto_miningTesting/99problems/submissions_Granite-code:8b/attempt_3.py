import math
def nearest_price(n):
 if n % 100 == 0:
 return n + 99 - (n % 99)
 else:
 remainder = n % 100
 return n + (100 - remainder) - (n % 99)
n = int(input())
nearest_price = nearest_price(n)
print(nearest_price)