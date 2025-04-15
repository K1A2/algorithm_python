import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

q = deque()
visited = [[0] * n for _ in range(n)]
q.append((r1, c1, 0))
visited[r1][c1] = 1

dxy = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
while q:
    x, y, count = q.popleft()
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if nx == r2 and ny == c2:
                print(count + 1)
                exit()
            q.append((nx, ny, count + 1))
print(-1)
