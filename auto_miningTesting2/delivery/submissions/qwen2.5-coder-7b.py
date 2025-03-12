def min_travel_distance(N, K, deliveries):
    # Sort deliveries by their location
    deliveries.sort()
    
    # Initialize DP table
    dp = [[float('inf')] * (K + 1) for _ in range(N)]
    dp[0][deliveries[0][1]] = abs(deliveries[0][0])
    
    for i in range(1, N):
        x_i, t_i = deliveries[i]
        prefix_sum = [0] * (K + 1)
        prefix_sum[t_i] = abs(x_i - deliveries[i-1][0]) * 2
        for j in range(K - t_i + 1):
            prefix_sum[j + t_i] = min(prefix_sum[j + t_i], prefix_sum[j] + abs(x_i - deliveries[i-1][0]) * 2)
        
        for j in range(K, -1, -1):
            if dp[i-1][j] != float('inf'):
                for k in range(max(0, K - j), min(K, t_i) + 1):
                    dp[i][j + k] = min(dp[i][j + k], dp[i-1][j] + prefix_sum[k])
    
    # Find the minimum distance to return to the origin with any remaining capacity
    result = float('inf')
    for j in range(K + 1):
        if dp[N-1][j] != float('inf'):
            result = min(result, dp[N-1][j] + abs(deliveries[-1][0]))
    
    return int(result)

# Read input
N, K = map(int, input().split())
deliveries = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(min_travel_distance(N, K, deliveries))