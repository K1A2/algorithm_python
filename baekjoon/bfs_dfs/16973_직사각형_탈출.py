from collections import deque
n, m = map(int,  input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())
walls = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            walls.append((i, j))
sc -= 1
sr -= 1
fr -= 1
fc -= 1

q = deque()
visited[sr][sc] = 1
q.append((sr, sc, 0))
while q:
    x, y, c = q.pop()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and 0 <= nx + h <= n and 0 <= ny + w <= m and visited[nx][ny] == 0:
            wall = 0
            for wx, wy in walls:
                if nx <= wx < nx + h and ny <= wy < ny + w:
                    wall = 1
                    break
            if wall: continue

            if nx == fr and ny == fc:
                print(c + 1)
                exit(0)

            visited[nx][ny] = 1
            q.appendleft((nx, ny, c + 1))
print(-1)
