import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0] = 1

while q:
    x, y, count = q.popleft()
    for i in range(1, data[x][y] + 1):
        for j in range(2):
            nx = x
            ny = y
            if j == 0:
                nx += i
            else:
                ny += i
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if nx == n - 1 and ny == m - 1:
                    print(count + 1)
                    exit()
                q.append((nx, ny, count + 1))
