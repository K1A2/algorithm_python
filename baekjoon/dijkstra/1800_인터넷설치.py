import sys
import heapq
INF = 10e9
input = sys.stdin.readline

n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [[INF] * (k + 1) for _ in range(n + 1)]
q = []
heapq.heappush(q, (0, 1, 0))
distance[1][0] = 0
while q:
    dist, now, skip = heapq.heappop(q)
    if distance[now][skip] < dist: continue
    for n_node, n_dist in graph[now]:
        if skip < k and distance[n_node][skip + 1] > dist:
            distance[n_node][skip + 1] = dist
            heapq.heappush(q, (dist, n_node, skip + 1))
        n_max = max(n_dist, dist)
        if distance[n_node][skip] > n_max:
            distance[n_node][skip] = n_max
            heapq.heappush(q, (n_max, n_node, skip))

if distance[n][k] == INF:
    print(-1)
else:
    print(distance[n][k])
