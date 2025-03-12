def move_left(grid):
    new_grid = [[0]*4 for _ in range(4)]
   
    for i in range(4):
        filler = 0
        for j in range(4):
            if grid[i][j]!=0:
                if new_grid[i][filler]==0:
                    new_grid[i][filler] = grid[i][j]
                elif new_grid[i][filler]==grid[i][j]:
                    new_grid[i][filler]*=2
                    filler+=1
                else:
                    filler+=1
                    new_grid[i][filler] = grid[i][j]
    return new_grid
   
def rotate(grid):
    new_grid = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    return new_grid
   
def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3-j])
    return new_grid
   
def get_grid():
    grid = []
    for _ in range(4):
        grid.append(list(map(int, input().strip().split())))
    return grid

grid = get_grid()
move = int(input().strip())

for _ in range(move):
    grid = rotate(grid)
grid = reverse(grid)
grid = move_left(grid)
grid = reverse(grid)
for _ in range(4-move):
    grid = rotate(grid)

for i in range(4):
    for j in range(4):
        print(grid[i][j], end=' ')
    print()