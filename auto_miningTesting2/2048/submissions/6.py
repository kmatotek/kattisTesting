def transpose(grid):
    return [list(row) for row in zip(*grid)]

def reverse(grid):
    return [row[::-1] for row in grid]

def merge(grid):
    for i in range(4):
        row = [v for v in grid[i] if v]
        for _ in range(len(row)-1):
            if row[_] == row[_+1]:
                row[_] *= 2
                row[_+1] = 0
        grid[i] = [v for v in row if v] + [0 for _ in range(4-len(row))]
    return grid

def move(grid, direction):
    transposed = False
    reversed = False

    if direction == 1:  # Up
        grid = transpose(grid)
        transposed = True
    elif direction == 2:  # Right
        grid = reverse(grid)
        reversed = True
    elif direction == 3:  # Down
        grid = reverse(transpose(grid))
        transposed = True
        reversed = True

    grid = merge(grid)

    if reversed:
        grid = reverse(grid)
    if transposed:
        grid = transpose(grid)

    return grid

grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

direction = int(input())
grid = move(grid, direction)

for row in grid:
    print(' '.join(map(str, row)))