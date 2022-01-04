from collections import deque
from sys import stdin
v, m = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[b].append(a)
def bfs(graph, node, visit_code):
    visited[node] = visit_code
    count = 0
    que = deque()
    que.append(node)
    while que:
        now = que.popleft()
        for n in graph[now]:
            if visited[n] == visit_code:
                continue
            count += 1
            visited[n] = visit_code
            que.append(n)
    return count
p = []
m = 0
for i in range(1, v + 1):
    c = bfs(graph, i, i)
    if m == c:
        p.append(i)
    elif m < c:
        p.clear()
        m = c
        p.append(i)
p.sort()
for i in p: print(i)