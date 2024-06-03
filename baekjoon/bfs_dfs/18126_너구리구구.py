import sys
from collections import deque
input = lambda : sys.stdin.readline()
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
ans = (1, 0)
q = deque()
q.append((1, 0))
visited[1] = 1
while q:
    node, dist = q.popleft()
    for n_node, n_dist in graph[node]:
        if not visited[n_node]:
            d = n_dist + dist
            q.append((n_node, d))
            visited[n_node] = 1
            if ans[1] < d:
                ans = (n_node, d)
print(ans[1])
