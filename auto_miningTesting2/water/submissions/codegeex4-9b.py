from collections import defaultdict, deque

def max_water_flow(n, p, k, initial_pipes, improvements):
    # Create graph to represent the network of water stations and pipes
    graph = defaultdict(lambda: defaultdict(int))
    
    # Add initial pipes to the graph
    for a, b, c in initial_pipes:
        graph[a][b] += c
        graph[b][a] += c
    
    # Function to perform BFS and find the maximum flow from source to sink
    def bfs(source, sink):
        parent = {}
        visited = set()
        
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                if neighbor not in visited and graph[current][neighbor] > 0:
                    parent[neighbor] = current
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
                    # If we reach the sink, break early
                    if neighbor == sink:
                        break
        
        # If no path was found, return 0
        if sink not in parent:
            return 0
        
        # Backtrack to find the path and calculate the flow
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities of the edges and reverse edges along the path
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        
        return path_flow
    
    # Function to calculate maximum flow using Edmonds-Karp algorithm (BFS-based)
    def max_flow(source, sink):
        total_flow = 0
        while True:
            flow = bfs(source, sink)
            if flow == 0:
                break
            total_flow += flow
        return total_flow
    
    # Calculate initial maximum flow
    initial_max_flow = max_flow(1, n)
    results = [initial_max_flow]
    
    # Process each improvement and calculate new maximum flow
    for a, b, c in improvements:
        graph[a][b] += c
        graph[b][a] += c
        results.append(max_flow(1, n))
    
    return results

# Example usage:
n = 3
p = 2
k = 1
initial_pipes = [(1, 3, 10), (2, 3, 1)]
improvements = [(2, 3, 15)]

print(max_water_flow(n, p, k, initial_pipes, improvements))