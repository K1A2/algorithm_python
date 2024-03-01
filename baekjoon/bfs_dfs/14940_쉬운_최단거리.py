import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
answer = []
start = (0, 0)
for i in range(n):
    row = []
    for j, num in enumerate(map(int, input().split())):
        row.append(num)
        if num == 2:
            start = (i, j)
    data.append(row)
    answer.append([-2] * m)
answer[start[0]][start[1]] = 0
q = deque()
q.append([start[0], start[1], 0])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
data[start[0]][start[1]] = -1
while q:
    x, y, distance = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and answer[nx][ny] == -2:
            answer[nx][ny] = distance + 1
            q.append([nx, ny, distance + 1])
            data[nx][ny] = -1
for i in range(n):
    for j in range(m):
        if answer[i][j] == -2:
            if data[i][j] == 0:
                answer[i][j] = 0
            if data[i][j] == 1:
                answer[i][j] = -1
for i in answer:
    print(*i)
