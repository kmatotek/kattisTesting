import random

def frogger(n, s, m, board):
    visited = [False]*n
    hops = 0
    current_square = s-1
    while True:
        if current_square >= n or current_square < 0:
            return 'left' if current_square<0 else 'right', hops
        elif board[current_square] == m:
            return 'magic', hops
        elif visited[current_square]:
            return 'cycle', hops
        visited[current_square] = True
        hops += 1
        current_square += board[current_square]

n, s, m = map(int, input().split())
board = list(map(int, input().split()))
fate, hops = frogger(n, s, m, board)
print(fate)
print(hops)