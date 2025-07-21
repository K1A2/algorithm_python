from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

points = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 'C']
(start_x, start_y), (end_x, end_y) = points

INF = 10e10
visited = [[[INF] * 4 for _ in range(m)] for __ in range(n)]

dq = deque()
for d in range(4):
    visited[start_x][start_y][d] = 0
    dq.append((start_x, start_y, d))

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))

while dq:
    x, y, dir = dq.popleft()
    cost = visited[x][y][dir]
    if (x, y) == (end_x, end_y):
        print(cost)
        sys.exit()

    for nd in range(4):
        nx = x + dxy[nd][0]
        ny = y + dxy[nd][1]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if board[nx][ny] == '*':
            continue

        new_cost = cost + (0 if nd == dir else 1)
        if new_cost < visited[nx][ny][nd]:
            visited[nx][ny][nd] = new_cost
            if nd == dir:
                dq.appendleft((nx, ny, nd))
            else:
                dq.append((nx, ny, nd))
print(-1)
