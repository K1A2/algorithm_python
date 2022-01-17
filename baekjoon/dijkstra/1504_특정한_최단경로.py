import sys
import heapq
INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().rstrip().split())
start1 = [1, v1, v2, n]
start2 = [1, v2, v1, n]

def dijkstra(start, distance, to):
    q = []
    heapq.heappush(q, (0, start))
    if distance[start] == INF:
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
    return distance[to]
result1 = result2 = 0
for i in range(len(start1) - 1):
    if result1 != INF:
        a = dijkstra(start1[i], distance[:], start1[i + 1])
        if a == INF:
            result1 = INF
            continue
        result1 += a
    if result2 != INF:
        a = dijkstra(start2[i], distance[:], start2[i + 1])
        if a == INF:
            result2 = INF
            continue
        result2 += a
if result2 == INF and result1 == INF:
    print(-1)
else:
    print(min(result1, result2))