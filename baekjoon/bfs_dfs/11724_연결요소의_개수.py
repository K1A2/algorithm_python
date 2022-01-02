from collections import deque
from sys import stdin
v, m = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(graph, node, visited):
    que = deque()
    que.append(node)
    while que:
        now = que.popleft()
        if visited[now]:
            continue
        visited[now] = 1
        for i in graph[now]:
            que.append(i)
count = 0
for i in range(1, v + 1):
    if len(graph[i]) != 0 and not visited[i]:
        count += 1
        bfs(graph, i, visited)
    elif len(graph[i]) == 0:
        count += 1
print(count)