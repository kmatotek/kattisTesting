def solve_jetpack_joyride(N, field):
    def is_obstacle(x, y):
        return field[y][x] == 'X'

    moves = []
    t = 0  # Current time
    x = 0  # Current column
    while x < N:
        # Check if there's an obstacle in the next square to the right
        if is_obstacle(x + 1, 9):
            # If there's an obstacle, we need to use the jetpack
            # Calculate how long we need to press the screen to jump over it
            press_duration = x - len(moves) * 2
            moves.append((t, press_duration))
            t += press_duration + 1  # Update time after pressing and lifting
        else:
            # If no obstacle, just move normally
            t += 1
        x += 1  # Move to the next column

    # Output the result
    print(len(moves))
    for (time, duration) in moves:
        print(time, duration)

# Read input
N = int(input().strip())
field = [input().strip() for _ in range(10)]

# Solve the problem
solve_jetpack_joyride(N, field)