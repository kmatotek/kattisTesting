n, s, m = map(int, input().split())
board = list(map(int, input().split()))

def hop(pos, direction):
    if direction == "right":
        pos += board[pos]
    else:
        pos -= abs(board[pos])
    return pos

pos = s
hops = 0
visited = set()

while True:
    hops += 1
    pos = hop(pos, "right" if board[pos] > 0 else "left")

    if pos in visited:
        print("cycle")
        print(hops)
        break

    if pos == m:
        print("magic")
        print(hops)
        break

    if pos < 1:
        print("left")
        print(hops)
        break

    if pos > n:
        print("right")
        print(hops)
        break

    visited.add(pos)