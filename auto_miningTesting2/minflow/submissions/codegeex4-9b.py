import sys
from heapq import heappop, heappush
from math import sqrt

def calculate_distance(junction1, junction2):
    return sqrt((junction1[0] - junction2[0]) ** 2 + (junction1[1] - junction2[1]) ** 2 + (junction1[2] - junction2[2]) ** 2)

def min_cost_to_connect_system(n, m, junctions, pipes):
    # Create adjacency list for the graph
    adj_list = {i: [] for i in range(1, n+1)}
    for pipe in pipes:
        a, b = pipe
        distance = calculate_distance(junctions[a-1], junctions[b-1])
        adj_list[a].append((b, distance))
        adj_list[b].append((a, distance))
    
    # Priority queue for Dijkstra's algorithm
    min_heap = [(0, 1)]  # (cost, start)
    costs = {i: float('inf') for i in range(1, n+1)}
    costs[1] = 0
    
    while min_heap:
        current_cost, u = heappop(min_heap)
        
        if current_cost > costs[u]:
            continue
        
        for v, weight in adj_list[u]:
            distance = calculate_distance(junctions[u-1], junctions[v-1])
            new_cost = current_cost + distance
            
            if new_cost < costs[v]:
                costs[v] = new_cost
                heappush(min_heap, (new_cost, v))
    
    # Calculate the minimum cost considering the number of open holes
    min_cost = costs[n]
    plug_costs = [0.5 * junctions[i][3] for i in range(n) if junctions[i][3] > 0]
    if plug_costs:
        min_cost += min(plug_costs)
    
    return min_cost

def process_input():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for case_number in range(1, t + 1):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        junctions = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            z = int(data[index + 2])
            k = int(data[index + 3])
            junctions.append((x, y, z, k))
            index += 4
        
        pipes = []
        for _ in range(m):
            a = int(data[index])
            b = int(data[index + 1])
            pipes.append((a, b))
            index += 2
        
        result = min_cost_to_connect_system(n, m, junctions, pipes)
        if result == float('inf'):
            results.append(f"Case {case_number}: impossible")
        else:
            results.append(f"Case {case_number}: {result:.4f}")
    
    for result in results:
        print(result)

process_input()