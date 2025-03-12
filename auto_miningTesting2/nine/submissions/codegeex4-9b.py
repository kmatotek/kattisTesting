def count_positive_numbers_without_n(d):
    MOD = 1000000007
    if d == 1:
        return 9
    elif d == 0:
        return 1
    else:
        return (pow(9, d - 1, MOD) + count_positive_numbers_without_n(d - 1)) % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        d = int(data[i])
        results.append(count_positive_numbers_without_n(d))
    for result in results:
        print(result)