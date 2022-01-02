from collections import deque

m, n, h = map(int, input().split())
data = []
queue = deque()
for z in range(h):
    mid = []
    for x in range(n):
        tomatos = list(map(int, input().split()))
        for y in range(m):
            if tomatos[y] == 1:
                queue.append((x, y, z, 0))
        mid.append(tomatos)
    data.append(mid)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    day = 0
    while queue:
        x, y, z, day = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and data[nz][nx][ny] == 0:
                data[nz][nx][ny] = 1
                queue.append((nx, ny, nz, day + 1))
    return day

day = bfs()

for l in data:
    for i in l:
        if 0 in i:
            print(-1)
            exit()
print(day)