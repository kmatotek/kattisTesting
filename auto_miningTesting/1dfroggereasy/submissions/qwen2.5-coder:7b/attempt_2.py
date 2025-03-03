def frogger_game(n, s, m, board):
    visited = [False] * (n + 1)
    position = s
    hops = 0
    
    while True:
        if visited[position]:
            fate = 'cycle'
            break
        visited[position] = True
        
        if board[position - 1] == m:
            fate = 'magic'
            break
        elif position == 1 and board[0] < 0:
            fate = 'left'
            break
        elif position == n and board[n - 1] > 0:
            fate = 'right'
            break
        
        if board[position - 1] > 0:
            position += board[position - 1]
        else:
            position -= abs(board[position - 1])
        
        hops += 1
        
        # Check if the new position is out of bounds
        if not (1 <= position <= n):
            break
    
    return fate, hops

# Read input
n, s, m = map(int, input().split())
board = list(map(int, input().split()))

# Get the result
fate, hops = frogger_game(n, s, m, board)

# Print output
print(fate)
print(hops)