n = int(input())
d = [list(input()) for _ in range(n)]
r = [0]
def count(dir):
    nx, ny = x + dir[0], y + dir[1]
    c = 0
    while 0 <= nx < n and 0 <= ny < n:
        if d[nx][ny] == '.': return 0
        elif d[nx][ny] == 'W': c += 1
        else: return c
        nx, ny = nx + dir[0], ny + dir[1]
    return 0
for x in range(n):
    for y in range(n):
        if d[x][y] == '.':
            count_all = sum([count(i) for i in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))])
            if r[0] < count_all: r = [count_all, y, x]
print(f'{r[1]} {r[2]}\n{r[0]}') if r != [0] else print('PASS')