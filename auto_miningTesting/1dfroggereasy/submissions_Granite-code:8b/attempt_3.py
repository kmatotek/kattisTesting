def play_frogger(n, s, m, board):
    visited = [False] * n # keep track of which squares have been visited
    current_square = s - 1 # convert index to zero-based index
    num_hops = 0 # keep track of the number of hops
    
    while True:
        if current_square < 0 or current_square >= n:
            return ('left', num_hops) if current_square < 0 else ('right', num_hops)
        if board[current_square] == m:
            return ('magic', num_hops)
        if visited[current_square]:
            return ('cycle', num_hops)
        
        visited[current_square] = True
        
        jump_distance = board[current_square]
        current_square += jump_distance
        num_hops += 1