def count_numbers_without_n(d):
    MOD = 1000000007
    if d == 1:
        return 9
    elif d == 2:
        return 81
    else:
        return (90 * pow(9, d-2, MOD)) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        d = int(data[i])
        result = count_numbers_without_n(d)
        results.append(result)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()