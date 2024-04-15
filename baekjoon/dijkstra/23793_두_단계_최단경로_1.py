import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
x, y, z = map(int, input().split())

def dijkstra(start, skip=-1):
    dist = [sys.maxsize for _ in range(n + 1)]
    q = [(0, start)]
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for n_node, n_cost in graph[node]:
            if n_node == skip:
                continue
            next_cost = cost + n_cost
            if next_cost < dist[n_node]:
                dist[n_node] = next_cost
                heapq.heappush(q, (next_cost, n_node))
    return dist

dist_x = dijkstra(x)
dist_y = dijkstra(y)
dist_skip = dijkstra(x, y)

dist_xy = -1
if dist_x[y] != sys.maxsize and dist_y[z] != sys.maxsize:
    dist_xy = dist_x[y] + dist_y[z]

print(dist_xy, dist_skip[z] if dist_skip[z] != sys.maxsize else -1)
