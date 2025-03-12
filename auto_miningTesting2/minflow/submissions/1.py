import heapq

def dist(j1, j2):
    return ((j1[0] - j2[0])**2 + (j1[1] - j2[1])**2 + (j1[2] - j2[2])**2)**0.5

N, M = map(int, input().split())
junctions = [list(map(int, input().split())) for _ in range(N)]
pipes = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N+1)]
for a, b in pipes:
    G[a].append((b, dist(junctions[a-1], junctions[b-1])))
    G[b].append((a, dist(junctions[a-1], junctions[b-1])))