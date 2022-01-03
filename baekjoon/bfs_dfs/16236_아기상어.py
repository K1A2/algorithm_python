from collections import deque
from sys import stdin
n = int(stdin.readline())
data = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
dxt = ((-1, 0), (0, -1), (0, 1), (1, 0))
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            sec = 0
            size = 2
            eat = 0
            data[i][j] = 0
            start = (i, j)
            can_eat = None
            next_pos = deque()
            visited_index = 1
            visited = [[0] * n for _ in range(n)]
            while start is not None:
                count = 1
                for d in dxt:
                    nx, ny = start[0] + d[0], start[1] + d[1]
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] < visited_index and data[nx][ny] <= size:
                        visited[nx][ny] += 1
                        next_pos.append((nx, ny))
                if len(next_pos) == 0:
                    start = None
                while next_pos:
                    for p in next_pos:
                        x, y = p[0], p[1]
                        if 0 < data[x][y] < size:
                            if can_eat is None:
                                can_eat = (x, y)
                            elif x < can_eat[0]:
                                can_eat = (x, y)
                            elif x == can_eat[0]:
                                if y < can_eat[1]:
                                    can_eat = (x, y)
                    if can_eat is not None:
                        x, y = can_eat
                        data[x][y] = 0
                        sec += count
                        next_pos.clear()
                        eat += 1
                        if size == eat:
                            eat = 0
                            size += 1
                        start = (x, y)
                        can_eat = None
                        visited_index += 1
                    else:
                        for _ in range(len(next_pos)):
                            x, y = next_pos.popleft()
                            for d in dxt:
                                nx, ny = x + d[0], y + d[1]
                                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] < visited_index and data[nx][ny] <= size:
                                    visited[nx][ny] += 1
                                    next_pos.append((nx, ny))
                        count += 1
                        start = None
            print(sec)
            exit()