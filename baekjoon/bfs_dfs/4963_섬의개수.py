from collections import deque
from sys import stdin
dxy = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1))
def bfs(map_data, x, y):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        if not map_data[x][y]:
            continue
        map_data[x][y] = 0
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny]:
                que.append((nx, ny))

while True:
    w, h = map(int, stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    map_data = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if map_data[i][j]:
                bfs(map_data, i, j)
                count += 1
    print(count)