from collections import deque
from sys import stdin
n, m = map(int, stdin.readline().split())
data = [[[-1, 1, i] for i in list(map(int, stdin.readline().rstrip()))] for _ in range(n)] # visited, count, type
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))

queue = deque()
save = deque()
queue.append((0, 0, 0, 2))
while queue:
    x, y, wall_breaked, index = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(data[x][y][1])
        exit()
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if (0 > nx or nx >= n) or (0 > ny or ny >= m) or data[nx][ny][0] == index:
            continue
        else:
            if data[nx][ny][2] == 1:
                if not wall_breaked: # 부순적 없는 벽
                    data[nx][ny][1] = data[x][y][1] + 1
                    data[nx][ny][2] = 2
                    if data[nx][ny][0] != index * -1:
                        queue.append((nx, ny, 1, index * -1))
                        data[nx][ny][0] = index * -1
                        save.append((x, y, 0, index))
            elif data[nx][ny][2] == 0:
                if index < 0 < data[nx][ny][0]:
                    if not queue and save:
                        s = save.popleft()
                        queue.append(s)
                        data[s[0]][s[1]][0] = s[3]
                    continue
                if data[nx][ny][0] != index:
                    data[nx][ny][1] = data[x][y][1] + 1
                    queue.append((nx, ny, wall_breaked, index))
                    data[nx][ny][0] = index
    if not queue and save:
        s = save.popleft()
        queue.append(s)
        data[s[0]][s[1]][0] = s[3]
print(-1)