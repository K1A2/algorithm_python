import sys
import heapq
import math
input = sys.stdin.readline
n, w = map(int, input().split())
m = float(input())
pos = [list(map(int, input().split())) for _ in range(n)]
graph = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):
    a, b = pos[i]
    for j in range(i + 1, n):
        c, d = pos[j]
        dis = math.sqrt((a - c) ** 2 + (b - d) ** 2)
        # if dis > m: continue
        graph[i][j] = dis
        graph[j][i] = dis
for i in [list(map(int, input().split())) for _ in range(w)]:
    a, b = i[0] - 1, i[1] - 1
    if graph[a][b] != sys.maxsize:
        graph[a][b] = 0
        graph[b][a] = 0

distance = [sys.maxsize] * n

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for idx, i in enumerate(graph[now]):
            cost = dist + i
            if cost < distance[idx]:
                distance[idx] = cost
                heapq.heappush(q, (cost, idx))

dijkstra(0)
if distance[-1] != sys.maxsize:
    print(int(distance[-1] * 1000))
else:
    print(-1)
