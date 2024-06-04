import sys
from collections import deque
input = lambda: sys.stdin.readline()
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
data = list(map(int, input().split()))

q = deque()
q.append((0, 0))
visited[0] = 1
ans = data[0]
while q:
    node, dist = q.popleft()
    for n_node in graph[node]:
        n_dist = dist + 1
        if not visited[n_node] and n_dist <= m:
            visited[n_node] = 1
            ans += data[n_node]
            q.append((n_node, n_dist))
print(ans)
