import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m, k = map(int, input().split())
data = [[0] * m for _ in range(n)]
for _ in range(k):
    a, b = map(lambda x: int(x) - 1, input().split())
    data[a][b] = 1

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if data[nx][ny] == 1:
                    count += 1
                    q.append((nx, ny))
    return count

ans = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and visited[i][j] == 0:
            ans = max(ans, bfs(i, j, visited))
print(ans)
