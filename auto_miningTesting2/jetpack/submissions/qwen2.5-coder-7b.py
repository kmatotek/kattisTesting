def solve_game(N, field):
    # Initialize variables
    moves = []
    t = 0
    x = 0
    jetpack_on = False
    
    # Starting position at the lower left corner of the center square
    row = 9
    col = 0
    
    while col < N:
        if jetpack_on:
            # Ascend diagonally up until reaching the ceiling or an obstacle
            while row > 0 and field[row-1][col] == '.':
                row -= 1
                t += 1
            
            # If we hit an obstacle, start falling down
            jetpack_on = False
        
        if not jetpack_on and field[row][col+1] == 'X':
            # Enable jetpack when about to hit an obstacle
            moves.append((t, x + 1))
            jetpack_on = True
            t += 1
            x = 0
        
        # Move to the right by one square per second
        col += 1
        t += 1
        x += 1
    
    return len(moves), moves

# Read input
N = int(input())
field = [input().strip() for _ in range(10)]

# Solve the game
P, moves = solve_game(N, field)

# Output the result
print(P)
for move in moves:
    print(*move)