#!/usr/bin/env python

n, s, m = map(int, input().split())
board = list(map(int, input().split()))

frog_index = s - 1
hop_count = 0
while True:
    if board[frog_index] > 0:
        hop_count += board[frog_index]
        frog_index = (frog_index + hop_count) % n
    elif board[frog_index] < 0:
        hop_count += abs(board[frog_index])
        frog_index = (frog_index - hop_count) % n
    else:
        break
if board[frog_index] == m:
    print("magic")
    print(hop_count)
else:
    if frog_index == 0:
        print("left")
        print(hop_count)
    elif frog_index == n - 1:
        print("right")
        print(hop_count)
    else:
        print("cycle")
        print(hop_count)