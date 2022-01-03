from collections import deque
from sys import stdin
v = int(stdin.readline())
p1, p2 = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(v + 1)]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(n):
    visited = [0] * (v + 1)
    que = deque()
    que.append((n, 0))
    while que:
        now, count = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                if i == p2:
                    return count + 1
                visited[i] = 1
                que.append((i, count + 1))
    return -1
print(bfs(p1))