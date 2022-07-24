import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    d = deque()
    d.append((1, 0))
    visited[1] = 1
    count = 0
    while d:
        now, level = d.popleft()
        for i in graph[now]:
            if not visited[i] and level + 1 <= 2:
                d.append((i, level + 1))
                visited[i] = 1
                count += 1
    return count

print(bfs())
