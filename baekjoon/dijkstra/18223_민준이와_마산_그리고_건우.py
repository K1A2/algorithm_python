import sys
import heapq
input = sys.stdin.readline
v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [sys.maxsize] * (v + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, d in graph[now]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance

d1 = dijkstra(1)[v]
d2 = dijkstra(1)[p] + dijkstra(p)[v]
if d2 <= d1:
    print('SAVE HIM')
else:
    print('GOOD BYE')
