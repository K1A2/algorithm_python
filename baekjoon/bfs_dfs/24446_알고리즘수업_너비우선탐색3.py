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
    graph[i] = sorted(graph[i], reverse=True)
order = [-1] * (n + 1)
count = 1
order[r] = 0

q = deque()
q.append((r, 0))
while q:
    now, depth = q.popleft()
    for next_node in graph[now]:
        if order[next_node] == -1:
            order[next_node] = depth + 1
            q.append((next_node, depth + 1))

for i in range(1, n + 1):
    print(order[i])
