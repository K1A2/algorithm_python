from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().rstrip().split())
data = [input().rstrip() for _ in range(n)]
visited = [[sys.maxsize] * m for _ in range(n)]

dxy = ((-1, 0), (1, 0), (0, 1), (0, -1))
def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0
    res = sys.maxsize
    while q:
        now_x, now_y = q.popleft()
        for d in dxy:
            nx = now_x + d[0]
            ny = now_y + d[1]
            while True:
                if not (0 <= nx < n and 0 <= ny < m): break
                if data[nx][ny] == '*': break
                if visited[nx][ny] < visited[now_x][now_y] + 1: break
                if data[nx][ny] == 'C':
                    res = min(res, visited[now_x][now_y] + 1)

                q.append((nx, ny))
                visited[nx][ny] = visited[now_x][now_y] + 1
                nx += d[0]
                ny += d[1]
    return res - 1

for x in range(n):
    for y in range(m):
        if data[x][y] == 'C':
            print(bfs(x, y))
            exit()