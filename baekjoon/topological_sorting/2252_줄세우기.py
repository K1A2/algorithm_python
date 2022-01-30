import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
count = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    count[b] += 1
q = deque()
for i in range(1, n + 1):
    if count[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    print(now, end=' ')
    nexts = graph[now]
    for i in nexts:
        count[i] -= 1
        if count[i] == 0:
            q.append(i)