def open_safe():
    # Read the initial configuration of the safe from input
    grid = [list(map(int, input().split())) for _ in range(3)]
    
    # Function to increment a digit and handle wrapping around
    def increment_digit(digit):
        return (digit + 1) % 4
    
    # Function to increment all digits in the same row
    def increment_row(row_index):
        for j in range(3):
            grid[row_index][j] = increment_digit(grid[row_index][j])
    
    # Function to increment all digits in the same column
    def increment_column(col_index):
        for i in range(3):
            grid[i][col_index] = increment_digit(grid[i][col_index])
    
    # Try to open the safe by pushing buttons until all digits are zero
    count = 0
    while True:
        try:
            # Find the first non-zero digit
            for i in range(3):
                for j in range(3):
                    if grid[i][j] != 0:
                        # Push the button at position (i, j)
                        increment_row(i)
                        increment_column(j)
                        count += 1
                        break
            else:
                # If no non-zero digit is found, the safe cannot be opened
                print(-1)
                return
            
            # Check if the safe is open
            if all(all(x == 0 for x in row) for row in grid):
                print(count)
                return
        
        except KeyboardInterrupt:
            # Optional: Allow interruption to stop the program gracefully
            print(count)
            return

open_safe()