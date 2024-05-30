import sys
from collections import deque
n = int(input())
data = list(map(int, input().split()))
s = int(input()) - 1

visited = [0] * n
q = deque()
q.append(s)
visited[s] = 1
while q:
    pos = q.popleft()
    delta = data[pos]
    for n_pos in [pos + delta, pos - delta]:
        if 0 <= n_pos < n and not visited[n_pos]:
            visited[n_pos] = 1
            q.append(n_pos)
print(sum(visited))
