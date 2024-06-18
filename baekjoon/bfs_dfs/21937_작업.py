import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
start = int(input())
ans = 0

d = deque()
d.append((start, 0))
visited[start] = 1
while d:
    node, cost = d.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = 1
            ans += 1
            d.append((i, cost + 1))
print(ans)
