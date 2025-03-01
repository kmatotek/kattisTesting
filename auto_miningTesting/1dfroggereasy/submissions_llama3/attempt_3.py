import sys

def get_frog_fate(n, s, m, board):
    if board[s-1] == m:
        return 'magic', 0
    hop_count = 0
    while True:
        if abs(board[s-1]) > 0:
            for i in range(1, abs(board[s-1])):
                s += 1 if board[s-1] > 0 else -1
        if set([s]) in [[i for i in range(1, n+1)]]:
            return 'cycle', hop_count + (abs(s - s) * (board[s-1] < 0))
        elif s <= 1:
            return 'left', hop_count
        elif s >= n:
            return 'right', hop_count
        hop_count += 1

n, s, m = map(int, input().split())
board = list(map(int, input().split()))
fate, hops = get_frog_fate(n, s, m, board)
print(fate)
print(hops)