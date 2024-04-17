import sys
import heapq
input = sys.stdin.readline
n, v, e = map(int, input().split())
a, b = map(int, input().split())
team = list(map(int, input().split()))
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))

def dijkstra(start):
    distance = [sys.maxsize] * (v + 1)
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n_node, n_dist in graph[node]:
            d = dist + n_dist
            if d < distance[n_node]:
                distance[n_node] = d
                heapq.heappush(q, (d, n_node))
    for i in range(v + 1):
        if distance[i] == sys.maxsize:
            distance[i] = -1
    return distance

kist = dijkstra(a)
seal = dijkstra(b)

ans = 0
for t in team:
    ans += kist[t] + seal[t]
print(ans)
