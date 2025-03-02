n = int(input())
if n % 10 == 5:
    print(n)
else:
    if (n + 99) % 100 == 99:
        print(n + 99)
    else:
        print(n + 99 - ((n + 99) % 100))