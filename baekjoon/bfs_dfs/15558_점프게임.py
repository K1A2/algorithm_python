from collections import deque
n, k = map(int, input().split())
line = [list(map(int, list(input()))) for _ in range(2)]
visited = [[0] * n for _ in range(2)]

q = deque()
q.append((0, 0, 0))
visited[0][0] = 1
dxy = ((0, -1), (0, 1), (1, k))

while q:
    x, y, time = q.pop()
    for dx, dy in dxy:
        nx = (x + dx) % 2
        ny = y + dy
        if 0 <= nx < 2 and 0 <= ny < n and visited[nx][ny] == 0 and ny > time and line[nx][ny] == 1:
            visited[nx][ny] = 1
            q.appendleft((nx, ny, time + 1))
        elif 0 <= nx < 2 and ny >= n:
            print(1)
            exit()
print(0)
