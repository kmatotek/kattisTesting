def compress(grid):
    # empty grid
    empty = [[0] * 4 for _ in range(4)]
    
    # here we shift entries of each cell to the extreme left row by row
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                empty[i][pos] = grid[i][j]
                pos += 1
    return empty


def merge(grid):
    for i in range(4):
        for j in range(3):
            # if current cell has same value as next cell and they are non empty then 
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                # double current cell value and empty the next cell
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
    return grid


def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3 - j])
    return new_grid

    
def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i])
    return new_grid


def apply_move(grid, move):
    # this function simulates 2048 game by applying a move up, down, left or right
    # 0: left, 1: up, 2: right, 3:down
    # left move
    if move == 0:
        # compress the grid after shifting cells to the left
        grid = compress(grid)
        # then merge the cells 
        grid = merge(grid)
        # and compress again after merging.
        grid = compress(grid)
    else:
        grid = transpose(grid)
        if move == 1:
            grid = compress(grid)
            grid = merge(grid)
            grid = compress(grid)
        else:
            grid = reverse(grid)
            grid = compress(grid)
            grid = merge(grid)
            grid = compress(grid)
            grid = reverse(grid)
        grid = transpose(grid)
        
    return grid


def game_2048(grid, *moves):
    for move in moves:
        apply_move(grid, move)
    return grid


# reads an integer from input and convert it to a move direction
def read_input():
    grid = [list(map(int, input().strip().split())) for _ in range(4)]
    move = int(input().strip())
    return grid, move


def main():
    grid, move = read_input()
    grid = apply_move(grid, move)
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()