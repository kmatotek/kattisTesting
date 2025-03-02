def stone_game(N):
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"

if __name__ == '__main__':
    N = int(input())
    print(stone_game(N))