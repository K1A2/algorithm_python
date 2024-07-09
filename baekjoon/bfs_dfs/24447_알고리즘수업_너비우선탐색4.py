import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])
depth = [-1] * (n + 1)
order = [0] * (n + 1)
count = 1
depth[r] = 0
order[r] = 1
order_now = 1

q = deque()
q.append((r, 0))
while q:
    now, now_depth = q.popleft()
    for next_node in graph[now]:
        if depth[next_node] == -1:
            order_now += 1
            order[next_node] = order_now
            depth[next_node] = now_depth + 1
            q.append((next_node, now_depth + 1))

res = 0
for i in range(1, n + 1):
    res += order[i] * depth[i]
print(res)
