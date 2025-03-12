def jetpack_joyride(N, field):
    moves = []
    position = 0
    state = 'ground'  # State can be 'ground', 'flying_up', or 'flying_down'
    time = 0
    
    for column in range(N):
        if state == 'ground':
            # Check each row in the current column from bottom to top
            for row in range(9, -1, -1):
                if field[row][column] == 'X':
                    break
                position = row
                time += 1
                if row == 0:
                    state = 'flying_up'
                    moves.append((time, 1))
                    break
        elif state == 'flying_up':
            # Continue flying up until the top is reached
            position = 9
            time += 1
            if column == N - 1 or field[9][column + 1] == 'X':
                state = 'ground'
        elif state == 'flying_down':
            # Check each row in the current column from top to bottom
            for row in range(0, 10):
                if field[row][column] == 'X':
                    break
                position = row
                time += 1
                if row == 9:
                    state = 'ground'
                    moves.append((time, 1))
                    break
    
    return len(moves), moves

# Reading input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
field = []
index = 1
for i in range(10):
    field.append(list(data[index]))
    index += 1

# Get the result
P, move_series = jetpack_joyride(N, field)

# Output the result
print(P)
for move in move_series:
    print(move[0], move[1])