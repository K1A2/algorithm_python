import sys
import heapq
INF = int(1e9)

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

for _ in range(int(input())):
    n, d, h = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for _ in range(d):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[b].append((a, c))

    dijkstra(h)
    dis = count = 0
    for i in distance:
        if i != INF:
            dis = max(i, dis)
            count += 1
    print(count, dis)