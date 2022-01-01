from collections import deque
from sys import stdin
n, m = map(int, stdin.readline().split())
data = [[[-1, 1, i] for i in list(map(int, stdin.readline().rstrip()))] for _ in range(n)] # visited, count, type
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = deque()
queue.append((0, 0, 0, 2))
save = deque()
while queue:
    x, y, wall_breaked, index = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(data[x][y][1])
        exit()
    if data[x][y][0] == index:
        if not queue and save:
            queue.append(save.popleft())
        continue
    data[x][y][0] = index
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if (0 > nx or nx >= n) or (0 > ny or ny >= m) or data[nx][ny][0] == index:
            continue
        else:
            if data[nx][ny][2] == 1:
                if not wall_breaked: # 분순적 없는 벽
                    data[nx][ny][1] = data[x][y][1] + 1
                    data[nx][ny][2] = 2
                    queue.append((nx, ny, 1, index * -1))
                    save.append((x, y, 0, index))
            elif data[nx][ny][2] == 0:
                if index < 0 < data[nx][ny][0]:
                    if not queue and save:
                        queue.append(save.popleft())
                    continue
                data[nx][ny][1] = data[x][y][1] + 1
                queue.append((nx, ny, wall_breaked, index))
    if not queue and save:
        queue.append(save.popleft())
print(-1)