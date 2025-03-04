def main():
    seats, groups = map(int, input().split())
    sizes = list(map(int, input().split()))
    count = 0
    for size in sizes:
        if seats >= size:
            seats -= size
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()