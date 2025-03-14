def slide_row_left(row):
    non_zero = [x for x in row if x != 0]
    merged = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(non_zero[i] * 2)
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1
    while len(merged) < 4:
        merged.append(0)
    return merged

def slide_row_right(row):
    non_zero = [x for x in row if x != 0]
    merged = []
    i = len(non_zero) - 1
    while i >= 0:
        if i > 0 and non_zero[i] == non_zero[i - 1]:
            merged.append(non_zero[i] * 2)
            i -= 2
        else:
            merged.append(non_zero[i])
            i -= 1
    while len(merged) < 4:
        merged.insert(0, 0)
    return merged

def slide_grid_left(grid):
    return [slide_row_left(row) for row in grid]

def slide_grid_right(grid):
    return [slide_row_right(row) for row in grid]

def transpose(grid):
    return [list(x) for x in zip(*grid)]

def rotate_clockwise(grid):
    return transpose(slide_grid_left(transpose(grid)))

def rotate_counterclockwise(grid):
    return transpose(slide_grid_right(transpose(grid)))

def apply_move(grid, move):
    if move == 0:
        new_grid = slide_grid_left(grid)
    elif move == 1:
        new_grid = rotate_clockwise(slide_grid_left(rotate_counterclockwise(grid)))
    elif move == 2:
        new_grid = slide_grid_right(grid)
    else:
        new_grid = rotate_counterclockwise(slide_grid_right(rotate_clockwise(grid)))
    
    return new_grid

def print_grid(grid):
    for row in grid:
        print(' '.join(str(x) if x != 0 else '0' for x in row))

# Read input
grid = []
for _ in range(4):
    grid.append([int(x) for x in input().split()])
move = int(input())

# Apply the move
new_grid = apply_move(grid, move)

# Print the output
print_grid(new_grid)