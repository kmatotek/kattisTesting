def frogger_game(n, s, m, board):
    visited = set()
    hop_count = 0
    
    while True:
        if s in visited or s < 1 or s > n:
            if s < 1:
                return 'left', hop_count
            elif s > n:
                return 'right', hop_count
            else:
                return 'cycle', hop_count
        visited.add(s)
        
        move = board[s-1]
        hop_count += 1
        
        if abs(move) == m:
            return 'magic', hop_count
        s += move

# Reading input
n, s, m = map(int, input().strip().split())
board = list(map(int, input().strip().split()))

# Get the result of the game
result, hops = frogger_game(n, s, m, board)

# Print the output
print(result)
print(hops)