from collections import deque
from sys import stdin
n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
master = [0] * (n + 1)
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(node):
    que = deque()
    que.append(node)
    while que:
        now = que.popleft()
        if visited[now]:
            continue
        visited[now] = 1
        for i in graph[now]:
            if visited[i]:
                continue
            master[i] = now
            que.append(i)
bfs(1)
for i in range(2, n + 1): print(master[i])