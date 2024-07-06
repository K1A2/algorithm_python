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
order = [0] * (n + 1)
count = 1
order[r] = 1

q = deque()
q.append(r)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if order[next_node] == 0:
            count += 1
            order[next_node] = count
            q.append(next_node)

for i in range(1, n + 1):
    print(order[i])
