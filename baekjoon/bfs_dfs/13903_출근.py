import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(r)]
dxy = [tuple(map(int, input().split())) for _ in range(int(input()))]

q = deque()
visited = [[0] * c for _ in range(r)]

for i in range(c):
    if blocks[0][i] == 1:
        q.append((0, i, 0))
        visited[0][i] = 1

while q:
    x, y, count = q.popleft()
    if x == r - 1:
        print(count)
        exit()
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < r and 0 <= ny < c and blocks[nx][ny] == 1 and visited[nx][ny] == 0:
            q.append((nx, ny, count + 1))
            visited[nx][ny] = 1
print(-1)
