def calculate_distance(junction1, junction2):
    """Calculates the Euclidean distance between two junctions."""
    x1, y1, z1 = junction1
    x2, y2, z2 = junction2
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

def find_lowest_cost_path(junctions, pipes, source, destination):
    """Finds the lowest cost path from source to destination using Dijkstra's algorithm."""
    num_junctions = len(junctions)
    distances = [float('inf')] * (num_junctions + 1)
    distances[source] = 0
    visited = [False] * (num_junctions + 1)
    previous = [None] * (num_junctions + 1)

    for _ in range(num_junctions):
        min_distance = float('inf')
        min_index = -1

        # Find the unvisited junction with the smallest tentative distance.
        for j in range(1, num_junctions + 1):
            if not visited[j] and distances[j] < min_distance:
                min_distance = distances[j]
                min_index = j

        if min_index == -1:
            break

        visited[min_index] = True

        # Update tentative distances for neighbors of the current junction.
        for neighbor in range(1, num_junctions + 1):
            if (min_index, neighbor) in pipes or (neighbor, min_index) in pipes:
                edge_weight = calculate_distance(junctions[min_index - 1], junctions[neighbor - 1])
                new_distance = distances[min_index] + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = min_index

    # Check if a path exists to the destination.
    if distances[destination] == float('inf'):
        return "impossible"

    # Calculate the total cost of the path, including plugging holes.
    total_cost = distances[destination]
    current_junction = destination
    while current_junction != source:
        total_cost += junctions[current_junction - 1][3] * 0.5  # Add cost of plugging holes.
        current_junction = previous[current_junction]
    total_cost += junctions[source - 1][3] * 0.5  # Add cost of plugging holes at the source.

    return f"{total_cost:.4f}"

# Input processing
case_number = 1
while True:
    try:
        num_junctions, num_pipes = map(int, input().split())
        junctions = []
        for _ in range(num_junctions):
            x, y, z, holes = map(int, input().split())
            junctions.append((x, y, z, holes))

        pipes = set()
        for _ in range(num_pipes):
            a, b = map(int, input().split())
            pipes.add((a, b))

        # Solve the problem and print the result.
        result = find_lowest_cost_path(junctions, pipes, 1, num_junctions)
        print(f"Case {case_number}: {result}")
        case_number += 1

    except EOFError:
        break