def calculate_distance(delivery_points, truck_capacity):
    """Calculates the minimum travel distance for mail delivery.

    Args:
      delivery_points: A list of tuples (location, letters) representing delivery points.
      truck_capacity: The maximum number of letters the truck can carry.

    Returns:
      The minimum total travel distance.
    """

    total_distance = 0
    current_location = 0
    truck_load = 0

    for i in range(len(delivery_points)):
        location, letters = delivery_points[i]

        # Load letters onto the truck
        truck_load += letters

        # If the truck is full or it's the last delivery point
        if truck_load >= truck_capacity or i == len(delivery_points) - 1:
            # Calculate the distance to the farthest point in the current trip
            farthest_point = location

            # Travel to the farthest point and back to the post office
            total_distance += 2 * abs(farthest_point - current_location)

            # Update the current location and reset the truck load
            current_location = 0
            truck_load = 0

    return total_distance


# Read input
num_deliveries, truck_capacity = map(int, input().split())
delivery_points = []
for _ in range(num_deliveries):
    location, letters = map(int, input().split())
    delivery_points.append((location, letters))

# Calculate and print the minimum distance
min_distance = calculate_distance(delivery_points, truck_capacity)
print(min_distance)
