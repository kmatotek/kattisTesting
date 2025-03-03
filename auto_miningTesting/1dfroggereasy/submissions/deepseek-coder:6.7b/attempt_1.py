def frogger(n, s, m, board):
    visited = [False] * (n + 1)
    position = s
    hops = 0
    
    while True:
        if not 1 <= position <= n or visited[position]:
            return 'cycle', hops
        
        visited[position] = True
        hop_length = board[position - 1]
        position += hop_length
        hops += 1
        
        if hop_length == m:
            return 'magic', hops
        elif position < 1:
            return 'left', hops
        elif position > n:
            return 'right', hops

n, s, m = map(int, input().split())
board = list(map(int, input().split()))
state, hops = frogger(n, s, m, board)
print(state)
print(hops)