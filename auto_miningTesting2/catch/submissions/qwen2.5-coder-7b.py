def max_probability_to_airport(m, n, k, buses):
    # Initialize DP array where dp[i] represents the probability of reaching station i on time
    dp = [0.0 for _ in range(n)]
    dp[0] = 1.0  # Starting at station 0
    
    for bus in buses:
        a, b, s, t, p = bus
        if t <= k:
            # If the bus arrives by time k, update the probability of reaching station b
            new_dp = [p * dp[a]] + dp[1:]
            dp[b] = max(dp[b], max(new_dp))
    
    return dp[1]

# Input reading
m, n = map(int, input().split())
k = int(input())
buses = []

for _ in range(m):
    a, b, s, t, p = map(float, input().split())
    buses.append((int(a), int(b), int(s), int(t), p))

# Calculate and print the result
result = max_probability_to_airport(m, n, k, buses)
print(f"{result:.6f}")