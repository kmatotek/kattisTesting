def nearest_price(N):
    if N % 100 == 0:
        return N + 99
    else:
        return N + (100 - N % 100)

N = int(input())
print(nearest_price(N))