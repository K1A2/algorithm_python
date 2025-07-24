import sys
import heapq
INF = int(1e10)
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF] * (n + 1)
count = [0] * (n + 1)
q = [(0, 1)]
while q:
    cost, node = heapq.heappop(q)
    if count[node] >= k: continue

    distance[node] = cost
    count[node] += 1

    for next_node, next_cost in graph[node]:
        n_cost = cost + next_cost
        heapq.heappush(q, (n_cost, next_node))
for i in range(1, n + 1):
    if count[i] < k:
        print(-1)
    else:
        print(distance[i])
