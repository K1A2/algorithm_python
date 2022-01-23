import sys
import heapq
n, m, x = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a - 1].append((b - 1, c))
def dijkstra(start):
    q = []
    distance = [INF] * n
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
go = []
for i in range(n):
    go.append(dijkstra(i)[x - 1])
back = dijkstra(x - 1)
print(max(go[i] + back[i] for i in range(n)))