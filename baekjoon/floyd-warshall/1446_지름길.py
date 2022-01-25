import sys
import heapq
n, d = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
distance = [INF] * (d + 1)
graph = [[] for _ in range((d + 1))]
for i in range(1, d + 1):
    graph[i - 1].append((i, 1))
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a > d or b > d:
        continue
    is_in = False
    for i in range(len(graph[a])):
        g = graph[a][i]
        if g[0] == b:
            if g[1] > c:
                graph[a][i] = (b, c)
                is_in = True
            break
    if not is_in:
        graph[a].append((b, c))

def dijkstra(start):
    q = []
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

dijkstra(0)
print(distance[d])