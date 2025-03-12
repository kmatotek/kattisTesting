def bfs(graph, source, sink, parent):
    visited = [False]*len(graph)
    queue=[]
    queue.append(source)
    visited[source] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind==sink:
                    return True
    return False

def initialize_graph(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def execute_improvements(graph, improvements):
    result = []
    parent = [-1]*len(graph)
    max_flow = 0
    while bfs(graph, 0, 1, parent):
        path_flow = float("Inf")
        s = 1
        while(s !=  0):
            path_flow = min (path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow +=  path_flow
        v = 1
        while(v !=  0):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        result.append(max_flow)
        if not improvements:
            break
        a, b, c = improvements.pop(0)
        graph[a-1][b-1] += c
        graph[b-1][a-1] += c
    return result


def water_distribution(n, p, k, pipes, improvements):
    graph = initialize_graph(n)
    for pipe in pipes:
        a, b, c = pipe
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
    return execute_improvements(graph, improvements)

print(water_distribution(4, 4, 1, [(1, 2, 10), (1, 3, 10), (2, 4, 10), (3, 4, 10)], [(2, 3, 1)]))