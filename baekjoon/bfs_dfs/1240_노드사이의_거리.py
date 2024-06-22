import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(m):
    a, b = map(int, input().split())
    visited = [0] * (n + 1)
    q = deque()
    q.append((a, 0))
    while q:
        node, dist = q.popleft()
        for n_node, n_dist in graph[node]:
            if visited[n_node] == 1:
                continue
            if n_node == b:
                print(dist + n_dist)
                q.clear()
                break
            visited[n_node] = 1
            q.append((n_node, n_dist + dist))
