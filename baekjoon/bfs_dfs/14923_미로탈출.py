import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
sx, sy = map(int, input().rstrip().split())
ex, ey = map(int, input().rstrip().split())
map_data = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dxy = ((-1, 0), (0, -1), (1, 0), (0, 1))

def bfs(x, y):
    q = deque()
    q.append((x, y, 1, 0))
    visited[x][y][1] = 1
    while q:
        x, y, magic, c = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][magic]:
                if nx == ex - 1 and ny == ey - 1:
                    return c + 1
                if map_data[nx][ny] and not visited[nx][ny][magic] and magic:
                    visited[nx][ny][0] = 1
                    q.append((nx, ny, 0, c + 1))
                elif not map_data[nx][ny]:
                    visited[nx][ny][magic] = 1
                    q.append((nx, ny, magic, c + 1))
    return -1
print(bfs(sx - 1, sy - 1))