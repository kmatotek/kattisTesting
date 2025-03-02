import sys

def main():
    N, M = map(int, input().split())
    sizes = list(map(int, input().split()))
    seats = [False] * N
    accepted = 0
    for size in sizes:
        if any(seats[i:i+size] for i in range(N-size+1)):
            continue
        seats[i:i+size] = [True] * size
        accepted += size

    print(M - accepted)

if __name__ == '__main__':
    main()