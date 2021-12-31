dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, m, n):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        if visited[x][y]:
            continue
        else:
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                    if not visited[nx][ny]:
                        queue.append((nx, ny))
                else:
                    continue

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1

    visited = [[False] * m for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and data[i][j] == 1:
                count += 1
                search(i, j, m, n)
    print(count)