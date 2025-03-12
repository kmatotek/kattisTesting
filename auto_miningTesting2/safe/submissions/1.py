def solve(d):
    pressed = 0
    for i in range(2,-1,-1):
        for j in range(3):
            press = (4 - d[i][j]) % 4
            pressed += press
            d = push(d, i, j, press)
    for row in d:
        if any(cell != 0 for cell in row):
            return -1
    return pressed

def push(d, x, y, times):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    d[x][y] = (d[x][y] + times) % 4
    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 3 and 0 <= ny < 3:
            d[nx][ny] = (d[nx][ny] + times) % 4
    return d
  
test_case = [[[3, 1, 2], [0, 1, 1], [3, 2, 3]]]
for case in test_case:
  result = solve(case)
  print("The number of times buttons should be pushed is ", result, ".") 