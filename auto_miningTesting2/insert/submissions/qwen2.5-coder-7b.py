def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_permutations(values):
    counts = {}
    for value in values:
        if value not in counts:
            counts[value] = 0
        counts[value] += 1
    
    numerator = factorial(len(values))
    denominator = 1
    for count in counts.values():
        denominator *= factorial(count)
    
    return numerator // denominator

def read_input():
    while True:
        N = int(input())
        if N == 0:
            break
        values = list(map(int, input().split()))
        yield values

def main():
    for values in read_input():
        print(count_permutations(values))

if __name__ == "__main__":
    main()