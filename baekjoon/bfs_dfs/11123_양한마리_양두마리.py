import sys
from collections import deque

def bfs(x, y, n, m, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and data[nx][ny] == '#':
                visited[nx][ny] = 1
                q.append((nx, ny))

input = lambda : sys.stdin.readline()
for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(input().rstrip()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and data[i][j] == '#':
                count += 1
                bfs(i, j, n, m, visited)
    print(count)
