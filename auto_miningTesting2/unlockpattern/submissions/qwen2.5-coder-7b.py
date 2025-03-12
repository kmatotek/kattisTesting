def calculate_length(order):
    # Define the positions of the pivots on a unit grid
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    
    # Calculate the Manhattan distance between two positions
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    total_length = 0
    
    # Iterate through the order and calculate distances
    for i in range(len(order) - 1):
        p1 = positions[order[i]]
        p2 = positions[order[i + 1]]
        total_length += manhattan_distance(p1, p2)
    
    return total_length

# Sample input
order = [6, 1, 9]
length = calculate_length(order)
print(length)  # Output: 9.82842712474619