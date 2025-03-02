def frogger_game(n, s, m, board):
    visited = [False] * n
    position = s - 1
    hops = 0

    while True:
        if board[position] == m:
            return 'magic', hops
        
        if hops >= len(board) or (position + 1 < 0) or (position + 1 > n - 1):
            return 'left' if position <= 0 else 'right'
        
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