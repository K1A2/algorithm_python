import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
watch = list(map(int, input().split()))
graph = [[] for _ in range(n)]
distance = [sys.maxsize] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    if (a != n - 1 and watch[a] == 1) or (b != n - 1 and watch[b] == 1):
        continue
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    q.append((0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            ndist = dist + next_dist
            if ndist < distance[next_node]:
                distance[next_node] = ndist
                heapq.heappush(q, (ndist, next_node))

dijkstra(0)
print(distance[-1] if distance[-1] != sys.maxsize else -1)
