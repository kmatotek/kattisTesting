def calculate_win_probability(N, V1, V2, W):
    P = [[0.0 for _ in range(V2+1)] for _ in range(N+1)]
    
    # Fill the DP table
    for i in range(1, N+1):
        for j in range(min(i+1, V2+1)):
            P[i][j] = 0.5 * (P[i-1][j-1] if j > 0 else 0) + 0.5 * (P[i-1][j])
    
    # Calculate the probability of winning
    win_prob = sum(P[N][i] for i in range(V2+1))
    
    return win_prob

def determine_action(N, V1, V2, W):
    W /= 100.0  # Convert percentage to decimal
    
    win_probability = calculate_win_probability(N, V1, V2, W)
    
    if win_probability > W:
        return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
    elif win_probability == W:
        return "PATIENCE, EVERYONE! (It's a tie)"
    else:
        return "RECOUNT!"

# Read input
T = int(input())
results = []
for _ in range(T):
    N, V1, V2, W = map(int, input().split())
    result = determine_action(N, V1, V2, W)
    results.append(result)

# Print output
for result in results:
    print(result)