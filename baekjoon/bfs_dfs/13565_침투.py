import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if not data[nx][ny] and not visited[nx][ny]:
                    if nx + 1 == n:
                        return 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 0

for i in range(m):
    if not visited[0][i] and not data[0][i]:
        r = bfs(0, i)
        if r:
            print('YES')
            exit()
print('NO')
