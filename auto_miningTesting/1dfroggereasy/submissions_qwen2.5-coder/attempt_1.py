def frogger_game(n, s, m, board):
    visited = [False] * n
    hops = 0
    current_square = s - 1
    
    while True:
        hops += 1
        if board[current_square] == m:
            return 'magic', hops
        next_square = current_square + board[current_square]
        
        if next_square < 0 or next_square >= n:
            return 'left' if next_square < 0 else 'right', hops
        
        if visited[next_square]:
            return 'cycle', hops
        
        visited[next_square] = True
        current_square = next_square

# Read input
n, s, m = map(int, input().split())
board = list(map(int, input().split()))

# Determine the frog's fate and number of hops
fate, h = frogger_game(n, s, m, board)

# Output the result
print(fate)
print(h)