import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
count_list = []

def count_space(x, y, idx):
    q = deque()
    q.append((x, y))
    count = 1
    data[x][y] = -idx
    while q:
        nx, ny = q.pop()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            qx = nx + dx
            qy = ny + dy
            if 0 <= qx < n and 0 <= qy < m and data[qx][qy] == 1:
                data[qx][qy] = -idx
                count += 1
                q.append((qx, qy))
    count_list.append(count)

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            count_space(i, j, len(count_list) + 1)

ans = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            ansc = 1
            counted = []
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                qx = i + dx
                qy = j + dy
                if 0 <= qx < n and 0 <= qy < m and data[qx][qy] < 0 and data[qx][qy] not in counted:
                    ansc += count_list[-data[qx][qy] - 1]
                    counted.append(data[qx][qy])
            ans = max(ans, ansc)
print(ans)
