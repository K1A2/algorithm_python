import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m, c = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().rstrip().split())
    graph[x].append((y, z))

def dijkstra(start):
    dis = [INF] * (n + 1)
    q = []
    dis[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis

dis = dijkstra(c)
count = res = 0
for i in dis:
    if i != INF:
        count += 1
        res = max(res, i)
print(count - 1, res)