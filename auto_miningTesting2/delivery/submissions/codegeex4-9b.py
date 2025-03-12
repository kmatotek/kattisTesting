def minimum_total_travel_distance(N, K, deliveries):
    # Initialize the current position at the post office (origin)
    current_position = 0
    total_distance = 0
    remaining_capacity = K
    
    # Sort deliveries by location to optimize the route
    deliveries.sort()
    
    # Iterate through each delivery point
    for location, letters in deliveries:
        # Check if the truck needs to return to the post office to reload
        if letters > remaining_capacity:
            # Calculate the distance to go back to the post office
            total_distance += 2 * current_position
            # Reset the truck's capacity and position
            remaining_capacity = K
            current_position = 0
        
        # Deliver the letters at the current location
        current_position = location
        remaining_capacity -= letters
    
    # After all deliveries, return to the post office
    total_distance += 2 * current_position
    return total_distance

# Reading input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

deliveries = []
index = 2
for _ in range(N):
    x_j = int(data[index])
    t_j = int(data[index + 1])
    deliveries.append((x_j, t_j))
    index += 2

# Calculate the minimum total travel distance
result = minimum_total_travel_distance(N, K, deliveries)
print(result)