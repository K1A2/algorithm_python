import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = dis + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance
found = False
for idx, i in enumerate(dijkstra(x)):
    if i == k:
        found = True
        print(idx)
if not found:
    print(-1)