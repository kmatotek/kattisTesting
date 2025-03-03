import sys
from collections import deque

def frogger(n, s, m):
    board = list(map(int, input().split()))
    pos = s
    moves = 0
    seen = set()
    while True:
        if pos == m:
            return "magic", moves
        elif pos < 1 or pos > n:
            return "right" if pos < 1 else "left", moves
        elif board[pos] < 0:
            pos += board[pos]
        else:
            moves += board[pos]
            seen.add(pos)
            pos = (pos + 1) % n
        if len(seen) == n and pos != m:
            return "magic", moves