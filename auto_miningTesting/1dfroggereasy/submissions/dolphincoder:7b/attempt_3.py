def frogger(n, s, board):
     # Initialize the frog's position and hop counter
    pos  = s - 1
    hops  = 0

     # Create a set to keep track of visited squares
    visited  = {pos}

    while True:
         # Check if the frog is on a positive or negative square
        if board[pos] > 0:
            new_pos  = pos + abs(board[pos])
            hop_dist  = abs(board[pos])
        elif board[pos] < 0:
            new_pos  = pos - abs(board[pos])
            hop_dist  = abs(board[pos])
        else:
             # End the game if the frog lands on a square with no hops
            return "magic", hops

         # Check for game end conditions
        if new_pos < 0 or new_pos >= n:
             # Left or right end of the board
            return "left" if new_pos < 0 else "right", hops
        elif pos in visited:
             # Cycle detected
            return "cycle", hops

         # Update the frog's position and hop counter
        pos = new_pos
        hops += hop_dist
        visited.add(new_pos)

    return "magic", hops