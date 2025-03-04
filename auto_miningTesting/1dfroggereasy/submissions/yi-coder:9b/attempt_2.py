def frogger():
    n, s, m = map(int, input().split())
    board = list(map(int, input().split()))

    pos = s - 1 # minus one as it's zero indexed
    hop_count = 0
    visited_positions = {pos}

    while True:
        jump_distance = board[pos]

        if jump_distance == m and pos != s - 1:
            print('magic')
            break
        elif jump_distance < 0:
            new_position = pos + abs(jump_distance)
            if new_position >= n:
                print('right')
                break
        else:
            new_position = pos + jump_distance
            if new_position < 0 or new_position >= n:
                print('left' if new_position < 0 else 'right')
                break

        pos = new_position if new_position < n else n - 1
        hop_count += 1

        if pos in visited_positions:
            print('cycle')
            break
        else:
            visited_positions.add(pos)

    print(hop_count)