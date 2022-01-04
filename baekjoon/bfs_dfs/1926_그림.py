from collections import deque
from sys import stdin
h, w = map(int, stdin.readline().rstrip().split())
data = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(x, y):
    que = deque()
    que.append((x, y))
    count = 1
    visited[x][y] = 1
    while que:
        x, y = que.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and data[nx][ny] == 1:
                que.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    return count
count = 0
m = 0
for i in range(h):
    for j in range(w):
        if not visited[i][j] and data[i][j]:
            count += 1
            r = bfs(i, j)
            if r > m:
                m = r
print(count)
print(m)