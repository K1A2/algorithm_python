from collections import deque

m, n = map(int, input().split())
data = []
queue = deque()
for x in range(n):
    tomatos = list(map(int, input().split()))
    for y in range(m):
        if tomatos[y] == 1:
            queue.append((x,y,0))
    data.append(tomatos)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    day = 0
    while queue:
        x, y, day = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                data[nx][ny] = 1
                queue.append((nx, ny, day + 1))
    return day

day = bfs()

for l in data:
    if 0 in l:
        print(-1)
        exit()
print(day)