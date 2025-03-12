def calculate_xp(current_level, x, d, c):
    if current_level >= d:
        return x
    else:
        return c * x

def max_xp(n, v, c, quests):
    # Initialize DP array where dp[i] is the maximum XP we can earn up to quest i
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        current_level = dp[i - 1] // v if dp[i - 1] > 0 else 0
        x, d = quests[i - 1]
        
        # Calculate XP without multiplier
        xp_without_multiplier = calculate_xp(current_level, x, d, c)
        
        # Calculate the new level after completing the quest without multiplier
        new_level_no_mul = current_level + xp_without_multiplier // v
        
        # Calculate XP with multiplier
        xp_with_multiplier = calculate_xp(current_level, x, d, c) * c
        
        # Calculate the new level after completing the quest with multiplier
        new_level_mul = current_level + (xp_with_multiplier - 1) // v
        
        # Update DP array considering both scenarios
        dp[i] = max(dp[i - 1], xp_without_multiplier + dp[new_level_no_mul] * v, xp_with_multiplier + dp[new_level_mul] * v)
    
    return dp[n]

# Read input
n, v, c = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the maximum XP
print(max_xp(n, v, c, quests))