def frogger_game(n, s, m, board):
    visited = [False] * n
    position = s - 1
    hops = 0

    while True:
        if board[position] == m:
            return 'magic', hops
        
        # Check if the new position is off the left end of the board
        if (position + board[position]) < 0:
            return 'left'
        
        # Check if the new position is off the right end of the board
        if (position + board[position]) >= n:
            return 'right'

        if visited[position]:
            return 'cycle', hops

        visited[position] = True
        move = board[position]
        position += move
        hops += 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    s = int(data[1])
    m = int(data[2])
    
    board = list(map(int, data[3:]))

    fate, hops = frogger_game(n, s, m, board)
    print(fate)
    print(hops)