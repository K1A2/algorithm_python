from collections import deque
from sys import stdin
h, w, case = map(int, stdin.readline().rstrip().split())
data = [[0] * w for _ in range(h)]
for i in range(case):
    sw, sh, ew, eh = map(int, stdin.readline().rstrip().split())
    for section_w in range(sw, ew):
        for section_h in range(sh, eh):
            data[section_h][section_w] = 1
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(x, y):
    que = deque()
    que.append((x, y))
    count = 0
    while que:
        x, y = que.popleft()
        if data[x][y]:
            continue
        data[x][y] = 1
        count += 1
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 0:
                que.append((nx, ny))
    return count
count = []
for i in range(h):
    for j in range(w):
        if not data[i][j]:
            count.append(bfs(i, j))
count.sort()
print(len(count))
for i in count: print(i, end=' ')