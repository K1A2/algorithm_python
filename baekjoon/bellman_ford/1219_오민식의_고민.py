import sys
from collections import deque
INF = int(1e10)
input = sys.stdin.readline
n, s, e, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
for x in edges:
    graph[x[0]].append(x[1])
income = list(map(int, input().split()))

dist = [INF] * n
dist[s] = -income[s]
for _ in range(n):
    for u, v, w in edges:
        w = -income[v] + w
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
if dist[e] == INF:
    print('gg')
    exit()

def dfs(snode):
    visited = [0] * n
    q = deque()
    q.append(snode)
    visited[snode] = 1
    while q:
        nn = q.pop()
        for nxn in graph[nn]:
            if visited[nxn] == 0:
                visited[nxn] = 1
                q.append(nxn)
    return visited[e] == 1

ex = 0
for u, v, w in edges:
    w = -income[v] + w
    if dist[u] != INF and dist[v] > dist[u] + w:
        if dfs(v):
            ex = 1
if ex:
    print('Gee')
    exit()

print(-dist[e])
