import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dxy = ((0, 1), (0, -1), (-1, 0), (1, 0))
def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1
    ans = 0
    while q:
        now_x, now_y = q.popleft()
        for d in dxy:
            nx = now_x + d[0]
            ny = now_y + d[1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[now_x][now_y] + 1
                q.append((nx, ny))
                ans = max(ans, visited[nx][ny])
    return ans - 1

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)
