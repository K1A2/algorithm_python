import sys
import heapq
input = sys.stdin.readline
dxy = ((0, -1), (-1, 0))
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x - 1 < 0 and y - 1 < 0: continue
        dis_save = [1e10] * 2
        for idx, d in enumerate(dxy):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n:
                if data[x][y] >= data[nx][ny]:
                    dis_save[idx] = dis[nx][ny] + data[x][y] - data[nx][ny] + 1
                else:
                    dis_save[idx] = dis[nx][ny]
        dis[x][y] = min(dis_save)
print(dis[-1][-1])
