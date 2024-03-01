import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
start = []
for i in range(n):
    inp = list(input())
    for j in range(m):
        if inp[j] == 'I':
            start = (i, j)
    data.append(inp)
q = deque([start])
data[start[0]][start[1]] = 'X'
count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 'X':
            if data[nx][ny] == 'P':
                count += 1
            data[nx][ny] = 'X'
            q.append((nx, ny))
print(count if count else 'TT')
