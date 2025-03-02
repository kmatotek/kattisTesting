def find_winner():
    N = int(input())
    if (N - 1) % 4 == 0:
        print("Bob")
    else:
        print("Alice")

find_winner()