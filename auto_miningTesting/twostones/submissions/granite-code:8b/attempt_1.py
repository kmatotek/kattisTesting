import sys
input = sys.stdin.readline

def optimal_stone_game(n):
    if n % 2 == 1:
        return "Alice"
    else:
        return "Bob"

if __name__ == "__main__":
    n = int(input())
    print(optimal_stone_game(n))