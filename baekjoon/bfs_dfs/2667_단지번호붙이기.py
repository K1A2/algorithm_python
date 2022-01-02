N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input())))

visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, s):
    visited[x][y] = True
    s += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
            if not visited[nx][ny]:
                s = search(nx, ny, s)
        else:
            continue
    return s

count = 0
size = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and data[i][j] == 1:
            count += 1
            size.append(search(i, j, 0))
print(count)
size.sort()
for i in size:
    print(i)