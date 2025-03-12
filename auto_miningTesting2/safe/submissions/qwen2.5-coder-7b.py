from collections import deque

def push_buttons(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Directions for pushing buttons in row, column and diagonal directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Initialize queue for BFS and set of visited states to avoid revisiting
    queue = deque([(grid, 0)])
    visited_states = set()
    visited_states.add(tuple(map(tuple, grid)))

    while queue:
        current_state, moves = queue.popleft()

        if all(all(cell == '0' for cell in row) for row in current_state):
            return moves

        # Try pushing each button
        for i in range(rows):
            for j in range(cols):
                new_state = [row[:] for row in current_state]
                
                # Increment the button being pushed and its surrounding cells
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        new_state[ni][nj] = str((int(new_state[ni][nj]) + 1) % 4)
                
                # Convert state to tuple for hashing and add to visited states
                state_tuple = tuple(map(tuple, new_state))
                if state_tuple not in visited_states:
                    visited_states.add(state_tuple)
                    queue.append((new_state, moves + 1))

    return -1

# Test the function with sample inputs
grid1 = [['3', '1', '2'], ['0', '1', '1'], ['3', '2', '3']]
print(push_buttons(grid1))  # Output: 4

grid2 = [['0', '0', '3'], ['2', '2', '3'], ['2', '2', '1']]
print(push_buttons(grid2))  # Output: -1