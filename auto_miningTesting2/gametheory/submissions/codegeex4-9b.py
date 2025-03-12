def soccat_game(C, test_cases):
    results = []
    for n, p, a in test_cases:
        # Initialize the dp array with zeros
        dp = [0] * n
        
        # Process each cell from right to left
        for i in range(n-1, -1, -1):
            # Calculate the maximum score if starting from this cell
            max_score = float('-inf')
            
            # Try all possible moves
            j = i
            while j < n:
                # Update the dp value based on the current move
                dp[i] = max(dp[i], a[j] - dp[j])
                
                # Move to the next position
                j += p[j]
            
            # Append the result for this starting position
            results.append(dp[i])
    
    return results

# Example usage:
C = 2
test_cases = [
    (10, [3, 1, 5, 2, 4, 9, 6, 10, 8, 7], [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]),
    (4, [4, 3, 2, 1], [3, 2, 3, 3])
]

output = soccat_game(C, test_cases)
for result in output:
    print(' '.join(map(str, result)))