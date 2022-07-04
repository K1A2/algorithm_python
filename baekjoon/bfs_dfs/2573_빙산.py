from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [[[i, 0, -1] for i in map(int, input().rstrip().split())] for _ in range(n)]

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs(x, y, visited_code, code):
    q = deque()
    q.append((x, y))
    data[x][y][2] = visited_code
    while q:
        now_x, now_y = q.popleft()
        zero_count = 0
        for d in dxy:
            nx, ny = now_x + d[0], now_y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if not data[nx][ny][code]:
                    zero_count += 1
                else:
                    if data[nx][ny][2] < visited_code:
                        data[nx][ny][2] = visited_code
                        q.append((nx, ny))
        if data[now_x][now_y][code] >= zero_count:
            data[now_x][now_y][(code + 1) % 2] = data[now_x][now_y][code] - zero_count
        else:
            data[now_x][now_y][(code + 1) % 2] = 0

count = 0
code = 0
while 1:
    found = not_melt = 0
    for x in range(n):
        for y in range(m):
            if data[x][y][2] < count:
                if data[x][y][code]:
                    if found:
                        print(count)
                        exit()
                    bfs(x, y, count, code)
                    found = 1
                    not_melt = 1
                else:
                    data[x][y][(code + 1) % 2] = 0
    if not not_melt:
        print(0)
        exit()
    code = (code + 1) % 2
    count += 1