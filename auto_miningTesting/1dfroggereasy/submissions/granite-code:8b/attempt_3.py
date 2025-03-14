import random
def play_game(n, s, m, board):
    fate = None
    hops = 0
    visited = set()
    while True:
        if board[s-1] == m:
            fate = "magic"
            break
        elif s < 1 or s > n:
            fate = "left" if s < 1 else "right"
            break
        elif s in visited:
            fate = "cycle"
            break
        else:
            visited.add(s)
            k = board[s-1]
            if k >= 0:
                s += k
            else:
                s += abs(k)
            hops += 1
    return fate, hops
n = int(input("Enter the number of board squares: "))
s = int(input("Enter the index of the frog's starting square: "))
m = int(input("Enter the magic number: "))
board = list(map(int, input("Enter the numbers in the board squares (separated by spaces): ").split()))
fate, hops = play_game(n, s, m, board)
print("Frog's fate:", fate)
print("Number of hops:", hops)