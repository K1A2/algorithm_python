import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if data[nx][ny] == '#':
                    q.append((nx, ny))

count = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == '#' and visited[i][j] == 0:
            count += 1
            dfs(i, j)
print(count)
