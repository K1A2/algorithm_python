import sys
from collections import deque
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

def dfs(x, y, mark):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if data[nx][ny] == mark:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    count += 1
    return count
ans = {'W': 0, 'B': 0}
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            ans[data[i][j]] += dfs(i, j, data[i][j]) ** 2
print(*list(ans.values()))
