import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [sys.maxsize] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
s, t = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n_node, n_dist in graph[node]:
            new_dist = n_dist + dist
            if new_dist < distance[n_node]:
                distance[n_node] = new_dist
                heapq.heappush(q, (new_dist, n_node))

dijkstra(s - 1)
print(distance[t - 1])
