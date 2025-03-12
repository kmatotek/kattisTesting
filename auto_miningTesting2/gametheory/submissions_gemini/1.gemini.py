def calculate_final_score(num_cells, cell_values, score_values):
    """
    Calculates the final score of the game for each starting cell, assuming optimal play.

    Args:
        num_cells: The number of cells in the row.
        cell_values: A list of integers representing the values written on the cells.
        score_values: A list of integers representing the score associated with each cell.

    Returns:
        A list of integers, where the i-th integer represents the final score of the game
        if the token starts on the i-th cell.
    """

    final_scores = [-1] * (num_cells + 1)  # Initialize with -1 to track computed scores
    
    def get_optimal_score(current_cell):
        """
        Recursively calculates the optimal score from a given cell.

        Args:
            current_cell: The index of the current cell.

        Returns:
            The optimal score achievable from the current cell.
        """
        
        if current_cell > num_cells:
            return 0
        if final_scores[current_cell] != -1:
            return final_scores[current_cell]

        max_score = float('-inf')  # Initialize with negative infinity for maximization
        for jump in range(1, num_cells + 1):
            next_cell = current_cell + jump * cell_values[current_cell - 1]
            if next_cell <= num_cells:
                opponent_score = get_optimal_score(next_cell)
                max_score = max(max_score, score_values[current_cell - 1] + opponent_score)
        
        final_scores[current_cell] = max_score
        return max_score

    for start_cell in range(1, num_cells + 1):
        final_scores[start_cell] = get_optimal_score(start_cell)

    return final_scores[1:]  # Return scores for starting cells 1 to n


# Read and process test cases
num_test_cases = int(input())
for _ in range(num_test_cases):
    num_cells = int(input())
    cell_values = list(map(int, input().split()))
    score_values = list(map(int, input().split()))
    
    # Calculate and print the results
    results = calculate_final_score(num_cells, cell_values, score_values)
    print(*results)