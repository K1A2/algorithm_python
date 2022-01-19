import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [[[i, 0] for i in list(map(int, sys.stdin.readline().rstrip().split()))] for _ in range(n)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def find_melt(visited):
    q = deque()
    q.append((0, 0))
    data[0][0][1] = visited
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny][0] == 0:
                    if data[nx][ny][1] < visited:
                        data[nx][ny][1] = visited
                        q.append((nx, ny))
                else:
                    data[nx][ny][1] += 1
    melt_all = True
    for x in range(n):
        for y in range(m):
            if data[x][y][0]:
                melt_all = False
                if data[x][y][1] > 1:
                    data[x][y][0] = 0
                data[x][y][1] = 0
    return melt_all
count = 1
while not find_melt(count):
    count += 1
print(count - 1)