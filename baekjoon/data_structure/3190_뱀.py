import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
data = [[0] * n for _ in range(n)]
data[0][0] = 1
for _ in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    data[x - 1][y - 1] = 2
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir_num = 0
now = (0, 0)
snake = deque()
snake.append((0, 0))
sec = 0

def set_direction(str, dir_num):
    if str == 'D':
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num + 3) % 4
    return dir_num

for _ in range(int(sys.stdin.readline().rstrip())):
    s, d = sys.stdin.readline().rstrip().split()
    s = int(s)
    s -= sec
    for _ in range(s):
        sec += 1
        nx = now[0] + dir[dir_num][0]
        ny = now[1] + dir[dir_num][1]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 2:
                data[nx][ny] = 1
                snake.append((nx, ny))
            elif data[nx][ny] == 0:
                data[nx][ny] = 1
                snake.append((nx, ny))
                tail = snake.popleft()
                data[tail[0]][tail[1]] = 0
            else:
                print(sec)
                exit()
            now = (nx, ny)
        else:
            print(sec)
            exit()
    dir_num = set_direction(d, dir_num)

while True:
    sec += 1
    nx = now[0] + dir[dir_num][0]
    ny = now[1] + dir[dir_num][1]
    if 0 <= nx < n and 0 <= ny < n:
        if data[nx][ny] == 2:
            data[nx][ny] = 1
            snake.append((nx, ny))
        elif data[nx][ny] == 0:
            data[nx][ny] = 1
            snake.append((nx, ny))
            tail = snake.popleft()
            data[tail[0]][tail[1]] = 0
        else:
            print(sec)
            exit()
        now = (nx, ny)
    else:
        print(sec)
        exit()