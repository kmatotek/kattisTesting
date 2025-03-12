def jetpack_joyride(n, field):
    stack = [0]*(2*n)
    top = 0
    base = 4
    for i in range(n):
        while base < 9 and field[base+1][i] == '.':
            base += 1
        while field[base][i] == '.':
            stack[top] = i
            top += 1
            base -= 1
        while top > 0 and stack[top-1] == i:
            top -= 1
            base += 1
    moves = []
    for i in range(1, top):
        if stack[i-1] != stack[i] - 1:
            moves.append((stack[i-1] + 1, stack[i] - stack[i-1] - 1))
    moves.append((stack[top-1] + 1, n - stack[top-1]))
    return moves

def main():
    n = int(input().strip())
    field = [list(input().strip()) for _ in range(10)]
    moves = jetpack_joyride(n, field)
    print(len(moves))
    for t, x in moves:
        print(t, x)

if __name__ == "__main__":
    main()