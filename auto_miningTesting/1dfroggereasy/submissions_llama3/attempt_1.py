import sys

def get_frog_fate(n, s, m, board):
    frog_pos = s
    hop_count = 0
    while True:
        if board[frog_pos-1] == m:
            return 'magic', hop_count
        elif frog_pos <= 1:
            return 'left', hop_count
        elif frog_pos >= n:
            return 'right', hop_count
        for i in range(1, abs(board[frog_pos-1])):
            frog_pos += 1 if board[frog_pos-1] > 0 else -1
        if board[frog_pos-1] == m:
            return 'magic', hop_count
        if set([frog_pos]) in [[i for i in range(1, n+1)]]:
            return 'cycle', hop_count + 1
        hop_count += 1

n, s, m = map(int, input().split())
board = list(map(int, input().split()))
fate, hops = get_frog_fate(n, s, m, board)
print(fate)
print(hops)