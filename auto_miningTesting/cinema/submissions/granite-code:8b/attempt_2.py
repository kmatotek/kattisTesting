def main():
    N, M = map(int, input().split())
    groups = list(map(int, input().split()))
    num_accepted = 0

    for group in groups:
        if N - sum(groups[:num_accepted]) >= group:
            num_accepted += 1

    print(M - num_accepted)


if __name__ == "__main__":
    main()