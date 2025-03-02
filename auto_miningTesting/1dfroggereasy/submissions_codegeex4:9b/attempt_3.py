def frogger_game(n, s, m, board):
    visited = set()
    position = s - 1
    hops = 0

    while True:
        if board[position] == m:
            return "magic", hops

        if position < 0 or position >= n:
            return ("left" if position < 0 else "right", hops)

        if position in visited:
            return "cycle", hops

        visited.add(position)
        hops += 1
        position += board[position]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = int(data[1])
    m = int(data[2])
    board = list(map(int, data[3:]))
    
    result, hops = frogger_game(n, s, m, board)
    print(result)
    print(hops)

if __name__ == "__main__":
    main()