import heapq
import sys
def add_edge(frm, to, depart, arrive, prob):
    adj[frm].append((to, depart, arrive, prob))
    
def get_max_prob(node, time):
    if dp[node][time] != -1:
        return dp[node][time]
    if node == 1:
        return 1.0
    if time == 0:
        return 0.0
    max_prob = 0.0
    for to, depart, arrive, prob in adj[node]:
        if depart < time:
            max_prob = max(max_prob, prob * get_max_prob(to, arrive))
    dp[node][time] = max(max_prob, get_max_prob(node, time - 1))
    return dp[node][time]
    
input_data = sys.stdin.readline

n, m = map(int, input_data().split())
k = int(input_data())
dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    a, b, s, t, p = map(float, input_data().split())
    a, b, s, t = int(a), int(b), int(s), int(t)
    edges.append((a, b, s, t, p))
edges.sort(key=lambda x: -x[2])
for a, b, s, t, p in edges:
    add_edge(a, b, s, t, p)
print("%.9f" % get_max_prob(0, k))