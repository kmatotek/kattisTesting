def start_game(matrix, direction):
    if direction == 0:    
        return move_and_merge_from_left(matrix)
    elif direction == 1:
        return move_and_merge_from_top(matrix)
    elif direction == 2:    
        return move_and_merge_from_right(matrix)
    else:                   
        return move_and_merge_from_bottom(matrix)

def move_and_merge_from_left(board):
    for i in range(4):
        temp = []
        flag = 0
        prev = 0
        
        for j in range(4):
            if board[i][j] != 0:
                if prev == 0:
                    prev = board[i][j]
                elif prev == board[i][j]:
                    temp.append(2*prev)
                    prev = 0
                    flag = 1
                    continue
                else:
                    temp.append(prev)
                    prev = board[i][j]
                
        if flag == 1 and prev != 0:
            temp.append(prev)

        if flag == 0:
            if prev != 0:
                temp.append(prev)

        while(len(temp) < 4):
            temp.append(0)

        board[i] = temp
    return board

def move_and_merge_from_right(board):
    return list(
        reversed(
            move_and_merge_from_left(
                list(
                    reversed(board)
                )
            )
        )
    )
def move_and_merge_from_top(board):
    return list(
        map(
            list, 
            zip(
                *move_and_merge_from_left(
                    list(
                        zip(*board)
                    )
                )
            )
        )
    )

def move_and_merge_from_bottom(board):
    return list(
        map(
            list, 
            zip(
                *move_and_merge_from_right(
                    list(
                        zip(*board)
                    )
                )
            )
        )
    )

grid = []
for _ in range(4):
    grid.append(list(map(int,input().strip().split())))

direction = int(input().strip())
            
result = start_game(grid, direction)

for line in result:
    print(*line)