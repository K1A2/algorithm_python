import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [list(str(input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dxy = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
def dfs(x, y):
    target = data[x][y]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.pop()
        for d in dxy[0 if target == '-' else 1]:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and target == data[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            dfs(i, j)
print(count)
