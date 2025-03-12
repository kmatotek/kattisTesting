import sys

def merge(line):
    non_zeros = [i for i in line if i != 0] # filter zeros
    for i in range(len(non_zeros)-1):
        if non_zeros[i] == non_zeros[i+1]: # if neighbor elements are equal
            non_zeros[i] *= 2               # double current element
            non_zeros[i+1] = 0              # set neighbor element to zero
    non_zeros = [i for i in non_zeros if i != 0] # filter newly made zeros
    non_zeros += [0] * (len(line) - len(non_zeros)) # fill the rest with zeros
    return non_zeros

# read input
board = [list(map(int, input().split())) for _ in range(4)]
move = int(input().strip())

if move == 0: # left
    board = [merge(row) for row in board]
elif move == 1: # up
    board = [merge(list(row)) for row in zip(*board)]
    board = [list(row) for row in zip(*board)] # transpose back to original orientation
elif move == 2: # right
    board = [merge(row[::-1])[::-1] for row in board]
elif move == 3: # down
    board = [merge(list(row[::-1]))[::-1] for row in zip(*board)]
    board = [list(row) for row in zip(*board)] # transpose back to original orientation

# print new state
for row in board:
    print(' '.join(map(str, row)))