def postal_delivery(n, k, deliveries):
    # Initialize the dp array where dp[j] is the minimum distance to deliver mail with j capacity left in the truck
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # No cost if no mail needs to be delivered
    
    # Process each delivery location
    for loc, load in deliveries:
        # Traverse from the current capacity backwards to prevent overwriting results of this round
        for j in range(k - load, -1, -1):
            if dp[j] != float('inf'):
                new_cost = dp[j] + 2 * abs(loc)  # Cost to deliver all mail at this location and return
                if new_cost < dp[j + load]:
                    dp[j + load] = new_cost
    
    # The answer is the minimum cost to deliver all mail and return with no capacity left in the truck
    return dp[k]

# Input reading
n, k = map(int, input().split())
deliveries = []
for _ in range(n):
    x, t = map(int, input().split())
    deliveries.append((x, t))

# Calculate the minimum travel distance
result = postal_delivery(n, k, deliveries)
print(result)