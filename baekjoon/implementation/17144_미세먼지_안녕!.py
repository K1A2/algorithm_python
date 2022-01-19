import sys
r, c, t = map(int, sys.stdin.readline().rstrip().split())
data = [[[i, 0] for i in list(map(int, sys.stdin.readline().rstrip().split()))] for _ in range(r)]
for x in range(r):
    if data[x][0][0] == -1:
        cleaner = (x, x + 1)
        break
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def diffusion(x, y):
    count = 0
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < r and 0 <= ny < c and data[nx][ny][0] != -1:
            data[nx][ny][1] += data[x][y][0] // 5
            count += 1
    data[x][y][0] -= data[x][y][0] // 5 * count
def wind(x, pos):
    dxy = (0, 1)
    now = (x, 1)
    tmp = 0
    while now != (x, 0):
        tmp2 = data[now[0]][now[1]][0]
        data[now[0]][now[1]][0] = tmp
        tmp = tmp2
        nx = now[0] + dxy[0]
        ny = now[1] + dxy[1]
        if ny >= c:
            if pos == 'u':
                dxy = (-1, 0)
            else:
                dxy = (1, 0)
        elif nx >= r or nx < 0:
            dxy = (0, -1)
        elif ny < 0:
            if pos == 'u':
                dxy = (1, 0)
            else:
                dxy = (-1, 0)
        now = (now[0] + dxy[0], now[1] + dxy[1])
time = 0
while time < t:
    for x in range(r):
        for y in range(c):
            if data[x][y][0] > 0:
                diffusion(x, y)
    for x in range(r):
        for y in range(c):
            data[x][y][0] += data[x][y][1]
            data[x][y][1] = 0
    wind(cleaner[0], 'u')
    wind(cleaner[1], 'd')
    time += 1
result = 0
for x in range(r):
    for y in range(c):
        if data[x][y][0] > 0:
            result += data[x][y][0]
print(result)