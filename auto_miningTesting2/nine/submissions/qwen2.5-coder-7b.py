MOD = 1_000_000_007

def count_numbers(d, has_leading_zero):
    if d == 1:
        return int(not has_leading_zero) + 8
    else:
        return (9 * count_numbers(d - 1, False) + 8 * count_numbers(d - 1, True)) % MOD

def main():
    T = int(input())
    results = []
    for _ in range(T):
        d = int(input())
        result = count_numbers(d, True)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()