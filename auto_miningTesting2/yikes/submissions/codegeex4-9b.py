def can_max_cross(M, B, D, T):
    # Calculate the time it takes for Max to cross the road
    max_time = 10 / M
    
    # Check if Max can beat the first bicycle
    if D / B < max_time:
        return "Max beats the first bicycle"
    
    # Check for collisions with each bicycle
    for k in range(1, 11):
        bike_time = (2 * k + D) / B
        if bike_time < max_time:
            return f"Collision with bicycle {k}"
    
    # If no collision occurs, find the first bicycle after which Max can cross safely
    for k in range(10, -1, -1):
        safe_time = (2 * k + D) / B + T
        if safe_time > max_time:
            return f"Max crosses safely after bicycle {k}"
    
    return "This should never be printed"

# Read number of test cases
N = int(input())

# Process each test case
for _ in range(N):
    M = float(input())
    B = float(input())
    D = float(input())
    T = float(input())
    result = can_max_cross(M, B, D, T)
    print(result)