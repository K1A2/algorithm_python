from sys import stdin
from collections import deque

def bfs(graph, node, visited, type):
    section = 1
    que = deque()
    que.append(node)
    if type[node] == 0:
        type[node] = section
    while que:
        now = que.popleft()
        if visited[now]:
            continue
        visited[now] = True
        section = 2 if type[now] == 1 else 1
        for i in graph[now]:
            if type[i] != 0 and type[i] == type[now]:
                return False
            type[i] = section
            que.append(i)
    return True

for _ in range(int(stdin.readline())):
    v, e = map(int, stdin.readline().rstrip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        f, t = map(int, stdin.readline().rstrip().split())
        graph[f].append(t)
        graph[t].append(f)
    visited = [0] * (v + 1)
    type = [0] * (v + 1)
    isyes = True
    for i in range(1, v + 1):
        if len(graph[i]) != 0 and not visited[i]:
            if not bfs(graph, i, visited, type):
                print('NO')
                isyes = False
                break
    if isyes:
        print('YES')