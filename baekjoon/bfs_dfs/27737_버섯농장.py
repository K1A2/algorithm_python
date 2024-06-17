import math
import sys
from collections import deque
input = lambda: sys.stdin.readline()
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n:
                if not data[nx][ny] and not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return count

res = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and not data[i][j]:
            r = bfs(i, j)
            res += math.ceil(r / k)
if res > m or res == 0:
    print('IMPOSSIBLE')
else:
    print(f'POSSIBLE\n{m - res}')
