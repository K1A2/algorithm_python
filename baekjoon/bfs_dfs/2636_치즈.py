from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [[[i, 0] for i in map(int, input().rstrip().split())] for _ in range(n)]

dxy = ((1, 0), (-1, 0), (0, -1), (0, 1))
def bfs(v):
    q = deque()
    q.append((0, 0))
    data[0][0][1] = -v

    all_melt = 1
    cheeze_count = 0
    while q:
        now_x, now_y = q.popleft()
        for d in dxy:
            nx, ny = now_x + d[0], now_y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny][0]:
                    cheeze_count += 1
                    all_melt = 0
                    data[nx][ny][0] = 0
                    data[nx][ny][1] = -v
                else:
                    if data[nx][ny][1] > -v:
                        data[nx][ny][1] = -v
                        q.append((nx, ny))
    return all_melt, cheeze_count

time = 1
last_count = 0
while 1:
    is_all_melt, count = bfs(time)
    if is_all_melt:
        print(time - 1)
        print(last_count)
        break
    last_count = count
    time += 1