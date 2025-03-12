def jetpack_joyride():
    """
    Calculates the moves for Jetpack Joyride game to avoid obstacles.

    Returns:
        tuple: A tuple containing the number of moves and a list of moves.
    """

    num_columns = int(input())
    field_layout = [input() for _ in range(10)]

    current_row = 9  # Start from the bottom row
    current_column = 1  # Start from the second column
    moves = []
    move_count = 0

    while current_column < num_columns:
        # Check for obstacles in the next 3 columns
        obstacle_found = False
        for col_offset in range(1, 4):
            if current_column + col_offset <= num_columns and field_layout[current_row][current_column + col_offset - 1] == 'X':
                obstacle_found = True
                break

        if obstacle_found:
            # Calculate jump duration
            jump_duration = 2 * (9 - current_row) + 1  
            moves.append((current_column, jump_duration))
            move_count += 1
            current_column += jump_duration  
        else:
            current_column += 1

    return move_count, moves


if __name__ == "__main__":
    move_count, move_list = jetpack_joyride()
    print(move_count)
    for column, duration in move_list:
        print(column, duration)