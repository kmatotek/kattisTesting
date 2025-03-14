import sys

def dfs(junctions, pipes, source, visited, current_height):
    if junctions[source][3] == 0:  # No open holes in this junction
        return True
    
    for pipe in pipes:
        a, b = pipe
        if (source, b) not in visited and a == source:
            if current_height >= junctions[b][2]:
                visited.add((source, b))
                if dfs(junctions, pipes, b, visited, current_height):
                    return True
    
    for pipe in pipes:
        a, b = pipe
        if (source, b) not in visited and b == source:
            if current_height >= junctions[a][2]:
                visited.add((source, b))
                if dfs(junctions, pipes, a, visited, current_height):
                    return True
    
    return False

def dijkstra(junctions, pipes, source, destination):
    n = len(junctions)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        min_dist, u = heapq.heappop(pq)
        
        if u == destination:
            return min_dist
        
        if min_dist > dist[u]:
            continue
        
        for pipe in pipes:
            a, b = pipe
            if (u, b) not in visited and a == u:
                new_cost = dist[u] + abs(junctions[a][2] - junctions[b][2])
                if new_cost < dist[b]:
                    dist[b] = new_cost
                    heapq.heappush(pq, (new_cost, b))
            elif (u, b) not in visited and b == u:
                new_cost = dist[u] + abs(junctions[a][2] - junctions[b][2])
                if new_cost < dist[a]:
                    dist[a] = new_cost
                    heapq.heappush(pq, (new_cost, a))
    
    return float('inf')

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    case_num = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(case_num):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        junctions = []
        pipes = set()
        
        for i in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            z = int(data[index + 2])
            k = int(data[index + 3])
            junctions.append([x, y, z, k])
            index += 4
        
        for _ in range(M):
            a = int(data[index]) - 1
            b = int(data[index + 1]) - 1
            pipes.add((min(a, b), max(a, b)))
            index += 2
        
        source = 0
        destination = N - 1
        
        # Use DFS to check if we can connect the source to the destination
        visited = set()
        if not dfs(junctions, pipes, source, visited, junctions[source][2]):
            results.append("impossible")
            continue
        
        # Use Dijkstra's algorithm to find the minimum cost path
        min_cost = dijkstra(junctions, pipes, source, destination)
        
        if min_cost == float('inf'):
            results.append("impossible")
        else:
            results.append(f"{min_cost:.4f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()