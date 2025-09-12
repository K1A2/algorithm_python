data = [list(map(int, input().split())) for _ in range(19)]

dxy = ((0, 1), (1, 0), (1, 1), (-1, 1))

def find(x, y, idx):
    for dx, dy in dxy:
        sx, sy = x, y
        while 0 <= sx - dx < 19 and 0 <= sy - dy < 19 and data[sx - dx][sy - dy] == idx:
            sx -= dx
            sy -= dy

        cnt = 0
        tx, ty = sx, sy
        while 0 <= tx < 19 and 0 <= ty < 19 and data[tx][ty] == idx:
            cnt += 1
            tx += dx
            ty += dy

        if cnt == 5:
            return 1, sx, sy
    return 0,

for i in range(19):
    for j in range(19):
        if data[i][j] != 0:
            r = find(i, j, data[i][j])
            if r[0]:
                print(data[i][j])
                print(r[1] + 1, r[2] + 1)
                exit()
print(0)
