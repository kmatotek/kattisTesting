# Read input from standard input
n, frog_pos, magic_num = map(int, input().split())
squares = list(map(int, input().split()))
frog_pos -= 1  # Adjust for 0-indexing

# Initialize visited positions and hop counter
visited = [False]*n
hops = 0

while True:
    if frog_pos < 0 or frog_pos >= n:  # Frog falls off the board
        print("left" if frog_pos < 0 else "right")
        break

    if visited[frog_pos]:  # Frog is trapped in a cycle
        print("cycle")
        break

    visited[frog_pos] = True
    hops += 1

    hop_len = squares[frog_pos]
    frog_pos += hop_len if hop_len > 0 else -hop_len  # Adjust for negative numbers

    if squares[frog_pos] == magic_num:  # Frog finds the magic number
        print("magic")
        break

print(hops)