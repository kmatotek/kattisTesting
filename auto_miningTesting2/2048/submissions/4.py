import sys

def rotateRight(grid):
    return [list(reversed(x)) for x in zip(*grid)]

def rotateLeft(grid):
    return list(list(x)[::-1] for x in zip(*grid))

def merge(grid):
    newGrid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                newGrid[i][pos] = grid[i][j]
                pos += 1
        for j in range(pos, 4):
            newGrid[i][j] = 0
        for j in range(3):
            if newGrid[i][j] == newGrid[i][j + 1] and newGrid[i][j] != 0:
                newGrid[i][j] *= 2
                newGrid[i][j + 1] = 0
        pos = 0
        for j in range(4):
            if newGrid[i][j] != 0:
                newGrid[i][pos] = newGrid[i][j]
                pos += 1
        for j in range(pos, 4):
            newGrid[i][j] = 0
    return newGrid

def executeMove(move, grid):
    for _ in range(move):
        grid = rotateRight(grid)
    grid = merge(grid)
    for _ in range(4 - move):
        grid = rotateRight(grid)
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
move = int(sys.stdin.readline())

newGrid = executeMove(move, grid)

printGrid(newGrid)