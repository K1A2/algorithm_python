import sys
import heapq
input = sys.stdin.readline
INF = 10e10
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
idx = 0
while 1:
    n = int(input())
    idx += 1
    if not n: break
    data = [list(map(int, input().split())) for _ in range(n)]
    dis = [[INF] * n for _ in range(n)]
    dis[0][0] = data[0][0]
    q = []
    heapq.heappush(q, (dis[0][0], 0, 0))
    while q:
        now_dis, x, y = heapq.heappop(q)
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == INF:
                dis[nx][ny] = data[nx][ny] + dis[x][y]
                heapq.heappush(q, (dis[nx][ny], nx, ny))
    print(f'Problem {idx}: {dis[-1][-1]}')
