import sys
import heapq
INF = 10e9
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[INF] * (k + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1, 0))
for i in range(k + 1):
    distance[1][i] = 0

while q:
    dist, now, count = heapq.heappop(q)
    if distance[now][count] < dist: continue
    if count + 1 <= k:
        for next_node, next_dist in graph[now]:
            if distance[next_node][count + 1] > dist:
                distance[next_node][count + 1] = dist
                heapq.heappush(q, (dist, next_node, count + 1))
    for next_node, next_dist in graph[now]:
        if distance[next_node][count] > dist + next_dist:
            distance[next_node][count] = dist + next_dist
            heapq.heappush(q, (dist + next_dist, next_node, count))
ans = INF
for i in range(k + 1):
    ans = min(ans, distance[n][i])
print(ans)
