def find_winner():
    n = int(input().strip())
    if n % 2 == 0:
        print("Bob")
    else:
        print("Alice")

find_winner()