from sys import stdin
from collections import deque
n = int(input())
map_data = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
safe_area = 1
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(x, y, limit):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map_data[nx][ny] > limit:
                que.append((nx, ny))

for i in range(min([min(m) for m in map_data]), max([max(m) for m in map_data]) + 1):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for h in range(n):
        for w in range(n):
            if not visited[h][w] and map_data[h][w] > i:
                bfs(h, w, i)
                count += 1
    if safe_area < count:
        safe_area = count
print(safe_area)