import sys
import heapq
input = sys.stdin.readline
n, m, a, b, c = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x - 1].append((y - 1, z))
    graph[y - 1].append((x - 1, z))

distance = [sys.maxsize] * n
q = []
q.append((0, 0, a - 1))
distance[a - 1] = 0
visited = [[0] * n for _ in range(n)]
res = sys.maxsize
while q:
    max_cost, cost, node = heapq.heappop(q)
    if c < cost:
        continue
    for n_node, n_cost in graph[node]:
        dist = n_cost + distance[node]
        if dist <= c and not visited[node][n_node]:
            visited[node][n_node] = 1
            if n_node == b - 1:
                res = min(res, max(max_cost, n_cost))
            distance[n_node] = dist
            heapq.heappush(q, (max(max_cost, n_cost), dist, n_node))
print(-1 if res == sys.maxsize else res)
