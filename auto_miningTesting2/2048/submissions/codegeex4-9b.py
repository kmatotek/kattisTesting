def move_left(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        merge_occurred = False
        write_index = 0
        for j in range(4):
            if grid[i][j] != 0:
                if new_grid[i][write_index] == 0:
                    new_grid[i][write_index] = grid[i][j]
                elif new_grid[i][write_index] == grid[i][j] and not merge_occurred:
                    new_grid[i][write_index] *= 2
                    merge_occurred = True
                else:
                    write_index += 1
                    if write_index != j:
                        new_grid[i][write_index] = grid[i][j]
    return new_grid


def move_right(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        merge_occurred = False
        write_index = 3
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                if new_grid[i][write_index] == 0:
                    new_grid[i][write_index] = grid[i][j]
                elif new_grid[i][write_index] == grid[i][j] and not merge_occurred:
                    new_grid[i][write_index] *= 2
                    merge_occurred = True
                else:
                    write_index -= 1
                    if write_index != j:
                        new_grid[i][write_index] = grid[i][j]
    return new_grid


def move_up(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for j in range(4):
        merge_occurred = False
        write_index = 0
        for i in range(4):
            if grid[i][j] != 0:
                if new_grid[write_index][j] == 0:
                    new_grid[write_index][j] = grid[i][j]
                elif new_grid[write_index][j] == grid[i][j] and not merge_occurred:
                    new_grid[write_index][j] *= 2
                    merge_occurred = True
                else:
                    write_index += 1
                    if write_index != i:
                        new_grid[write_index][j] = grid[i][j]
    return new_grid


def move_down(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for j in range(4):
        merge_occurred = False
        write_index = 3
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                if new_grid[write_index][j] == 0:
                    new_grid[write_index][j] = grid[i][j]
                elif new_grid[write_index][j] == grid[i][j] and not merge_occurred:
                    new_grid[write_index][j] *= 2
                    merge_occurred = True
                else:
                    write_index -= 1
                    if write_index != i:
                        new_grid[write_index][j] = grid[i][j]
    return new_grid


def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    grid = []
    index = 0
    for _ in range(4):
        grid.append(list(map(int, data[index:index+4])))
        index += 4
    
    move = int(data[index])
    
    if move == 0:
        new_grid = move_left(grid)
    elif move == 1:
        new_grid = move_up(grid)
    elif move == 2:
        new_grid = move_right(grid)
    elif move == 3:
        new_grid = move_down(grid)
    
    print_grid(new_grid)


if __name__ == "__main__":
    main()