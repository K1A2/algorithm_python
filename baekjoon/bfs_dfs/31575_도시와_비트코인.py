import sys
from collections import deque
input = lambda : sys.stdin.readline()
m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dxy = ((1, 0), (0, 1))

q = deque()
q.append((0, 0))
visited[0][0] = 1
while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print('Yes')
        exit()
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
print('No')
