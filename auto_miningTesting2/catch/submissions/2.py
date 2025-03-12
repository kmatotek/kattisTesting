import heapq

def ride_to_icpc_finals(m, n, k, bus_info):
    edges = [[] for _ in range(n)]

    for a, b, s, t, p in bus_info:
        edges[a].append((b, s, t, p))

    for edge in edges:
        edge.sort(reverse = True)

    best_prob = [0] * n
    best_prob[0] = 1.0
    pq = [(-1.0, 0, k)]

    while pq:
        curr_prob, curr_node, curr_time = heapq.heappop(pq)
        curr_prob = -curr_prob

        if curr_prob < best_prob[curr_node]: continue

        for next_node, start_time, end_time, prob in edges[curr_node]:
            if start_time >= curr_time: continue

            next_prob = curr_prob * prob

            if next_prob > best_prob[next_node]:
                best_prob[next_node] = next_prob
                heapq.heappush(pq, (-next_prob, next_node, start_time))

    return best_prob[1]


# read input
m, n = map(int, input().split())
k = int(input())

bus_info = []

for _ in range(m):
    a, b, s, t, p = map(float, input().split())
    a, b, s, t = int(a), int(b), int(s), int(t)
    bus_info.append((a, b, s, t, p))

# compute and print result
result = ride_to_icpc_finals(m, n, k, bus_info)
print('{:.9f}'.format(result))