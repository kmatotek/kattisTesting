def optimal_game_score(n, p, a):
    # Initialize DP arrays for maximum and minimum scores
    dp_max = [0] * (n + 1)
    dp_min = [0] * (n + 1)

    def max_score(x):
        if dp_max[x] != 0:
            return dp_max[x]
        
        # Calculate the maximum score starting from cell x
        max_val = float('-inf')
        for k in range(p[x-1], n-x+1, p[x-1]):
            max_val = max(max_val, a[x-1] + min_score(x+k))
        
        dp_max[x] = max_val
        return dp_max[x]

    def min_score(x):
        if dp_min[x] != 0:
            return dp_min[x]
        
        # Calculate the minimum score starting from cell x
        min_val = float('inf')
        for k in range(p[x-1], n-x+1, p[x-1]):
            min_val = min(min_val, max_score(x+k))
        
        dp_min[x] = min_val
        return dp_min[x]

    # Calculate the final score for each starting position
    results = []
    for s in range(1, n + 1):
        results.append(max_score(s))

    return results

# Read input
C = int(input())
results = []

for _ in range(C):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    result = optimal_game_score(n, p, a)
    results.extend(result)

# Output the results
for result in results:
    print(" ".join(map(str, result)))