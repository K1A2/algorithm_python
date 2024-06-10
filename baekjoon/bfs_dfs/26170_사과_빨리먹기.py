import sys
from collections import deque

input = lambda: sys.stdin.readline()
data = [list(map(int, input().split())) for _ in range(5)]
pos = list(map(int, input().split()))
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(x, y, c, a, r):
    if a == 3:
        return min(r, c)
    origin = data[x][y]
    data[x][y] = -1
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or data[nx][ny] == -1:
            continue
        r = dfs(nx, ny, c + 1, a + data[nx][ny], r)
    data[x][y] = origin
    return r


result = dfs(pos[0], pos[1], 0, int(data[pos[0]][pos[1]] == 1), 1e10)
print(result if result != 1e10 else -1)
