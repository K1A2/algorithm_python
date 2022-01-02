from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().rstrip().split())
map_data = []
zero_zone = []
for i in range(n):
    a = list(map(int, stdin.readline().rstrip().split()))
    for j in range(m):
        if a[j] == 0:
            zero_zone.append((i, j))
    map_data.append(a)

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(map_data, walls):
    visited = [[0] * m for _ in range(n)]
    for w in walls:
        map_data[w[0]][w[1]] = 1
    for ver in range(n):
        for horiz in range(m):
            if not visited[ver][horiz] and map_data[ver][horiz] == 2:
                que = deque()
                que.append((ver, horiz))
                while que:
                    x, y = que.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = 1
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map_data[nx][ny] != 1:
                            map_data[nx][ny] = 2
                            que.append((nx, ny))
    count = 0
    for ver in map_data:
        for horiz in ver:
            if horiz == 0:
                count += 1
    return count

result = 0
for i in range(len(zero_zone)):
    for j in range(i + 1, len(zero_zone)):
        for k in range(j + 1, len(zero_zone)):
            r = bfs([l[:] for l in map_data], (zero_zone[i], zero_zone[j], zero_zone[k]))
            if r > result:
                result = r
print(result)