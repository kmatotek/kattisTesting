def shift_left(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        fill_pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                if new_grid[i][fill_pos] == 0:
                    new_grid[i][fill_pos] = grid[i][j]
                elif new_grid[i][fill_pos] == grid[i][j]:
                    new_grid[i][fill_pos] *= 2
                    fill_pos += 1
                else:
                    fill_pos += 1
                    new_grid[i][fill_pos] = grid[i][j]
    return new_grid

def rotate_clockwise(grid):
    return [[grid[3-j][i] for j in range(4)] for i in range(4)]

def play_2048(grid, move):
    if move == 0:  # Left
        new_grid = shift_left(grid)
    elif move == 1:  # Up
        new_grid = rotate_clockwise(rotate_clockwise(rotate_clockwise(shift_left(rotate_clockwise(grid)))))
    elif move == 2:  # Right
        new_grid = rotate_clockwise(rotate_clockwise(shift_left(rotate_clockwise(rotate_clockwise(grid)))))
    else:  # Down
        new_grid = rotate_clockwise(shift_left(rotate_clockwise(grid)))
    return new_grid

# Get grid input
grid = []
for _ in range(4):
    row = list(map(int, input().split()))
    grid.append(row)

# Get move input
move = int(input())

# Play the game
new_grid = play_2048(grid, move)

# Print the new grid
for row in new_grid:
    print(*row)