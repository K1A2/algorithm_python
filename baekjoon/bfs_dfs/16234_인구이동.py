from collections import deque
from sys import stdin
n, r, l = map(int, stdin.readline().rstrip().split())
map_data = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
opened = []
dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))
count = 0
while True:
    index = -1
    visited = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                index += 1
                visited[i][j] = index
                que = deque()
                que.append((i,j))
                p = map_data[i][j]
                country = 1
                while que:
                    x, y = que.popleft()
                    now_p = map_data[x][y]
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                            gap = now_p - map_data[nx][ny]
                            gap = -1 * gap if gap < 0 else gap
                            if r <= gap <= l:
                                visited[nx][ny] = index
                                que.append((nx, ny))
                                p += map_data[nx][ny]
                                country += 1
                if country > 1:
                    opened.append(p // country)
                else:
                    visited[i][j] = -1
                    index -= 1
    if len(opened) == 0:
        break
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1:
                map_data[i][j] = opened[visited[i][j]]
    opened.clear()
    count += 1
print(count)