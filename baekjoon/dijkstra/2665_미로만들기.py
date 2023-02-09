import sys
from collections import deque
INF = 10e9
input = sys.stdin.readline
n = int(input())
data = [list(map(lambda x: int(not bool(int(x))), list(input().rstrip()))) for _ in range(n)]
distance = [[INF] * n for _ in range(n)]

q = deque()
q.appendleft((0, 0))
distance[0][0] = 0

dxy = ((0, 1), (1, 0), (-1, 0), (0, -1))
while q:
    x, y = q.popleft()
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] == INF:
            distance[nx][ny] = distance[x][y] + data[x][y]
            if data[nx][ny]: q.append((nx, ny))
            else: q.appendleft((nx, ny))
print(distance[-1][-1])
