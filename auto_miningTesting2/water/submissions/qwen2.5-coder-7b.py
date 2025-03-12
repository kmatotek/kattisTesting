import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distance = [-1] * n
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, u = heapq.heappop(pq)
        
        if dist > distance[u]:
            continue
        
        for v, capacity in graph[u]:
            new_dist = dist + capacity
            
            if distance[v] == -1 or new_dist > distance[v]:
                distance[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return distance[end]

def add_capacity(graph, u, v, c):
    for i in range(len(graph[u])):
        if graph[u][i][0] == v:
            graph[u][i] = (v, max(graph[u][i][1], c))
            return
    graph[u].append((v, c))

def add_edge(graph, u, v, c):
    if not any(v in edges for _, edges in graph.items()):
        graph[v] = []
    graph[v].append((u, c))
    add_capacity(graph, u, v, c)

def solve(n, p, k, initial_pipes, improvements):
    graph = {1: []}
    
    # Initialize the graph with the initial pipes
    for a, b, c in initial_pipes:
        if not any(b in edges for _, edges in graph.items()):
            graph[b] = []
        graph[a].append((b, c))
        add_capacity(graph, a, b, c)
    
    results = [dijkstra(graph, 1, n)]
    
    for a, b, c in improvements:
        if (a, b) in [(u, v[0]) for u, v in graph.items()] or (b, a) in [(u, v[0]) for u, v in graph.items()]:
            add_capacity(graph, a, b, c)
        else:
            add_edge(graph, a, b, c)
        
        results.append(dijkstra(graph, 1, n))
    
    return results

# Read input
n, p, k = map(int, input().split())
initial_pipes = [tuple(map(int, input().split())) for _ in range(p)]
improvements = [tuple(map(int, input().split())) for _ in range(k)]

# Solve the problem and print results
results = solve(n, p, k, initial_pipes, improvements)
for result in results:
    print(result)