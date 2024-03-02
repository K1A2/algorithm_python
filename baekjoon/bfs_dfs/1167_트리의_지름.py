import sys
from collections import deque
input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    i = list(map(int, input().split()))
    nv = i[0]
    for j in range(1, len(i) - 1, 2):
        a, b = i[j], i[j + 1]
        graph[nv].append((a, b))
e1 = (0, 0)
visited = [-1] * (v + 1)
q = deque([(1, 0)])
visited[1] = 0
while q:
    now, dis = q.pop()
    for g in graph[now]:
        if visited[g[0]] == -1:
            q.append((g[0], dis + g[1]))
            visited[g[0]] = 0
            if g[1] + dis > e1[1]:
                e1 = (g[0], g[1] + dis)
q = deque([(e1[0], 0)])
visited[e1[0]] = -1
e1 = (0, 0)
while q:
    now, dis = q.pop()
    for g in graph[now]:
        if visited[g[0]] != -1:
            q.append((g[0], dis + g[1]))
            visited[g[0]] = -1
            if g[1] + dis > e1[1]:
                e1 = (g[0], g[1] + dis)
print(e1[1])
