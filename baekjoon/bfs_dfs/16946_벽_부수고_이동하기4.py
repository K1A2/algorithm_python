import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
target = []
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
            if 0 <= qx < n and 0 <= qy < m and data[qx][qy] == 0:
                data[qx][qy] = -idx
                count += 1
                q.append((qx, qy))
    count_list.append(count % 10)

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            target.append((i, j))
        elif data[i][j] == 0:
            count_space(i, j, len(count_list) + 1)
for i in range(n):
    line = ''
    for j in range(m):
        if data[i][j] == 1:
            ans = 1
            counted = []
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                qx = i + dx
                qy = j + dy
                if 0 <= qx < n and 0 <= qy < m and data[qx][qy] < 0 and data[qx][qy] not in counted:
                    ans += count_list[-data[qx][qy] - 1]
                    counted.append(data[qx][qy])
            line += str(ans % 10)
        else:
            line += '0'
    print(line)
