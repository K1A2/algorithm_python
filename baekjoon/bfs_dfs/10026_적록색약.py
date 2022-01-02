from sys import stdin
from collections import deque
n = int(stdin.readline())
picture = [list(stdin.readline().rstrip()) for _ in range(n)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(x, y, eye):
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
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if eye: # 색맹
                    if (picture[nx][ny] == 'R' or picture[nx][ny] == 'G') and \
                            (picture[x][y] == 'R' or picture[x][y] == 'G'):
                        que.append((nx, ny))
                    elif picture[nx][ny] == picture[x][y]:
                        que.append((nx, ny))
                else:
                    if picture[nx][ny] == picture[x][y]:
                        que.append((nx, ny))

for i in range(2):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k]:
                bfs(j, k, i)
                count += 1
    print(count, end=' ')