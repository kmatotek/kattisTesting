def calculate_probability_of_catching_plane(m, n, k, buses):
    from collections import defaultdict
    import heapq

    # Create a graph to represent the city map
    graph = defaultdict(list)

    # Process each bus and construct the graph
    for i in range(m):
        a, b, s, t, p = buses[i]
        if t <= k:  # Only consider buses that can reach the airport on time
            graph[a].append((b, s, t, p))

    # Priority queue to process stations based on the earliest arrival time
    pq = []
    # Dictionary to store the maximum probability of reaching each station by a certain time
    max_prob = defaultdict(lambda: -1)

    # Start from the first station with 100% probability at time 0
    heapq.heappush(pq, (0, 0, 1.0))  # (arrival_time, current_station, probability)

    while pq:
        arrival_time, current_station, probability = heapq.heappop(pq)

        # If we reach the airport station, return the probability
        if current_station == 1:
            return probability

        # Process each bus from the current station
        for destination, dep_time, arr_time, p in graph[current_station]:
            if arr_time <= k and max_prob[destination] < probability * p:
                max_prob[destination] = probability * p
                heapq.heappush(pq, (arr_time, destination, probability * p))

    # If no route to the airport was found
    return 0.0

# Input reading and processing
m, n = map(int, input().split())
k = int(input())
buses = []
for _ in range(m):
    buses.append(list(map(float, input().split())))

# Calculate the probability of catching the plane
result = calculate_probability_of_catching_plane(m, n, k, buses)
print(f"{result:.6f}")