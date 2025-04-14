import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dxy = ((1, 0), (0, 1))

def bfs():
	q = deque()
	q.append((0, 0))
	visited[0][0] = 1
	while q:
		x, y = q.popleft()
		can_go = data[x][y]
		for d in dxy:
			nx = x + d[0] * can_go
			ny = y + d[1] * can_go
			if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
				if data[nx][ny] == -1:
					print('HaruHaru')
					exit(0)
				visited[nx][ny] = 1
				q.append((nx, ny))
bfs()
print('Hing')

