import sys
import heapq
INF = int(1e10)
input = sys.stdin.readline

k, n, r = int(input()), int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, c, d = map(int, input().split())
    graph[a].append((b, c, d))
distance = [[INF] * (k + 1) for _ in range(n + 1)]
q = [(0, 0, 1)]
distance[1][0] = 0
while q:
    dist, pay, node = heapq.heappop(q)
    if distance[node][pay] < dist: continue
    for next_node, next_dist, next_pay in graph[node]:
        n_cost = next_dist + dist
        n_pay = next_pay + pay
        if n_pay <= k and distance[next_node][n_pay] > n_cost:
            distance[next_node][n_pay] = n_cost
            heapq.heappush(q, (n_cost, n_pay, next_node))
ans = min(distance[n])
print(-1 if ans == INF else ans)
