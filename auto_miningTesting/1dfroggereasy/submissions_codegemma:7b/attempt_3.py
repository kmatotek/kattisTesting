def frogger():
    n, s, m = map(int, input().split())
    board = list(map(int, input().split()))

    hops = 0
    position = s

    while True:
        hops += 1
        if board[position] == m:
            return "magic", hops
        elif board[position] > 0:
            position += board[position]
            if position > n:
                return "right", hops
        else:
            position -= abs(board[position])
            if position < 1:
                return "left", hops
        if position in visited:
            return "cycle", hops
        visited.add(position)

visited = set()
fate, hops = frogger()
print(fate)
print(hops)