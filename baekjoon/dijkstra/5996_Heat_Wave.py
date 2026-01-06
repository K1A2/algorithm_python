import sys
import heapq
input = sys.stdin.readline

t, c, s, e = map(int, input().split())
graph = [[] for _ in range(t + 1)]
for _ in range(c):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

INF = int(1e9)
q = []
distance = [INF] * (t + 1)
distance[s] = 0
heapq.heappush(q, (0, s))
while q:
    cur_dist, cur_node = heapq.heappop(q)
    if distance[cur_node] < cur_dist: continue
    for next_node, i in graph[cur_node]:
        next_dist = cur_dist + i
        if next_dist < distance[next_node]:
            distance[next_node] = next_dist
            heapq.heappush(q, (next_dist, next_node))
print(distance[e])
