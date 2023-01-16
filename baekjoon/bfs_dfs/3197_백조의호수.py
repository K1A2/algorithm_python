import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(r)]
ice_visited = [[-1] * c for _ in range(r)]
swan_visited = [[-1] * c for _ in range(r)]

water = deque()
will_melt = deque()
swan = deque()
will_swan = deque()

swan_pos = []
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            lake[i][j] = '.'
            swan_pos.append((i, j))

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
count = 0
def bfs_melt(is_init=0):
    while will_melt and not is_init:
        water.append(will_melt.pop())
    while water:
        x, y = water.popleft()
        lake[x][y] = '.'
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < r and 0 <= ny < c and ice_visited[nx][ny] != 1:
                if lake[nx][ny] == 'X' and ice_visited[nx][ny] != 2:
                    ice_visited[nx][ny] = 2
                    will_melt.append((nx, ny))
                elif lake[nx][ny] == '.':
                    water.append((nx, ny))
                    ice_visited[nx][ny] = 1

def bfs_swan():
    while will_swan:
        swan.append(will_swan.pop())
    while swan:
        x, y = swan.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < r and 0 <= ny < c and swan_visited[nx][ny] != 1:
                if nx == swan_pos[1][0] and ny == swan_pos[1][1]:
                    print(count)
                    exit()
                if lake[nx][ny] == 'X' and swan_visited[nx][ny] != 2:
                    swan_visited[nx][ny] = 2
                    will_swan.append((nx, ny))
                elif lake[nx][ny] == '.':
                    swan_visited[nx][ny] = 1
                    swan.append((nx, ny))

for i in range(r):
    for j in range(c):
        if lake[i][j] == '.' and ice_visited[i][j] == -1:
            ice_visited[i][j] = 1
            water.append((i, j))
            bfs_melt(1)

swan.append(swan_pos[0])
while 1:
    bfs_melt()
    count += 1
    bfs_swan()
