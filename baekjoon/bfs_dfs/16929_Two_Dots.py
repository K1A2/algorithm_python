import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def dfs(start_x, start_y, x, y, count):
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m and data[start_x][start_y] == data[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(start_x, start_y, nx, ny, count + 1)
                visited[nx][ny] = 0
            else:
                if start_x == nx and start_y == ny and count >= 4:
                    print('Yes')
                    exit()

for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(x, y, x, y, 1)
        visited[x][y] = 0
print('No')