import sys
import heapq
INF = int(1e10)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append(((a, c)))
distance = [INF] * (n + 1)
q = [(0, 1, -1)]
distance[1] = 0
while q:
    cost, node, prev_node = heapq.heappop(q)
    if distance[node] < cost: continue
    if prev_node != -1:
        path[node].append((prev_node, node))
    for next_node, next_cost in graph[node]:
        new_cost = next_cost + cost
        if distance[next_node] > new_cost:
            distance[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node, node))
count = 0
s = ''
for i in path:
    for j in i:
        count += 1
        s += f'{j[0]} {j[1]}\n'
print(count)
print(s)
