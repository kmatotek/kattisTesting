def closest_price(N):
    # If the input already ends with 99, return it directly
    if str(N)[-2:] == '99':
        return N

    # Calculate both nearest upper and lower number that ends with 99.
    lower = (N // 100) * 100 + 99 if N % 100 < 99 else ((N // 100)) * 100 + 99
    upper = (N // 100) * 100 + 99 if N % 100 > 99 else ((N // 100) + 1) * 100 + 99

    # Return the nearest or upper one in case of a tie.
    return lower if abs(N - lower) <= abs(N - upper) else upper

def main():
    N = int(input())
    print(closest_price(N))

if __name__ == "__main__":
    main()