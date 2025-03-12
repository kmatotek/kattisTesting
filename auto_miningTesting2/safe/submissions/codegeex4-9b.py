def open_safe():
    # Read the initial configuration of the safe from input
    grid = [list(map(int, input().split())) for _ in range(3)]
    
    # Check if the safe is already open
    if all(all(x == 0 for x in row) for row in grid):
        print(0)
        return
    
    # Initialize a variable to count the number of button pushes
    push_count = 0
    
    # Define a function to increment a digit and handle wrapping around
    def increment_digit(digit):
        return (digit + 1) % 4
    
    # Define a function to find the minimum number of increments needed for a row or column
    def min_increments(target, current):
        if target <= current:
            return current - target
        else:
            return 4 - (target - current)
    
    # Calculate the total increments needed for each row and column
    total_increments = 0
    for i in range(3):
        row_increments = sum(min_increments(0, grid[i][j]) for j in range(3))
        col_increments = sum(min_increments(0, grid[j][i]) for j in range(3))
        total_increments += row_increments + col_increments
    
    # If the total increments are less than or equal to zero, the safe cannot be opened
    if total_increments <= 0:
        print(-1)
        return
    
    # Calculate the number of button pushes needed
    push_count = (total_increments - 1) // 9 + 1
    
    # Output the result
    print(push_count)

# Call the function to execute
open_safe()