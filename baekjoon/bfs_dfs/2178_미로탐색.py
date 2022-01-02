n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] += maze[x][y]
                queue.append((nx, ny))
bfs(0,0)
print(maze[n - 1][m - 1])