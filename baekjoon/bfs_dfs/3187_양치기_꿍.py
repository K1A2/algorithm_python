import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def dfs(x, y, mark):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count_w = 0
    count_s = 0
    if mark == 'v': count_w += 1
    if mark == 'k': count_s += 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if data[nx][ny] == '#': continue
                if data[nx][ny] == 'v':
                    count_w += 1
                if data[nx][ny] == 'k':
                    count_s += 1
                q.append((nx, ny))
    return count_s, count_w
ans = [0, 0]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and data[i][j] != '#':
            s, w = dfs(i, j, data[i][j])
            if s > w:
                ans[0] += s
            else:
                ans[1] += w
print(*ans)
