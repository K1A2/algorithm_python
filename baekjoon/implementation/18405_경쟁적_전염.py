import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
q = []
nq = []
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            heapq.heappush(q, (data[i][j], i, j))
ts, tx, ty = map(int, input().split())
sec = 0
while q:
    if sec == ts:
        print(data[tx - 1][ty - 1])
        exit(0)
    b, x, y = heapq.heappop(q)
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = b
            heapq.heappush(nq, (b, nx, ny))
    if len(q) == 0 and len(nq) > 0:
        q = nq[:]
        nq = []
        sec += 1
print(data[tx - 1][ty - 1])
