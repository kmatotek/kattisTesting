def frogger(n, s, m, board):
    visited = [False] * (n + 1)
    position = s
    hops = 0
    
    while 1 <= position <= n and not visited[position]:
        visited[position] = True
        hop_length = board[position - 1]
        position += hop_length
        hops += 1
        
        if abs(hop_length) == m:
            return 'magic', hops
    
    return ('cycle' if position <= 0 or position > n else 'left' if position < 1 else 'right'), hops

n, s, m = map(int, input().split())
board = list(map(int, input().split()))
state, hops = frogger(n, s, m, board)
print(state)
print(hops)