import sys
r, c, m = map(int, sys.stdin.readline().rstrip().split())
sarks = []
data = [[[-1, -1] for _ in range(c)] for _ in range(r)]
for i in range(m):
    sr, sc, s, d, z = map(int, sys.stdin.readline().rstrip().split())
    sr -= 1
    sc -= 1
    d -= 1
    data[sr][sc][0] = i
    sarks.append([0, sr, sc, s, d, z])
res = 0
for i in range(c):
    for x in range(r):
        if data[x][i][0] != -1:
            sarks[data[x][i][0]][0] = 1
            res += sarks[data[x][i][0]][5]
            data[x][i][0] = -1
            break
    for j in range(m):
        a, x, y, s, d, z = sarks[j]
        if a:
            continue
        data[x][y][0] = -1
        if d < 2:
            ul = x
            ud = r - x - 1
            re = s % ((ud + ul) * 2)
            if d == 0:
                if ul + r - 1 < re:
                    x = r - 1 - (re - (ul + r - 1))
                elif ul < re:
                    x = re - ul
                    d = 1
                else:
                    x -= re
            else:
                if ud + r - 1 < re:
                    x = re - (ud + r - 1)
                elif ud < re:
                    x = r - (re - ud) - 1
                    d = 0
                else:
                    x += re
        else:
            ul = y
            ur = c - y - 1
            re = s % ((ur + ul) * 2)
            if d == 2:
                if ur + c - 1 < re:
                    y = re - (ur + c - 1)
                elif ur < re:
                    y = c - (re - ur) - 1
                    d = 3
                else:
                    y += re
            else:
                if ul + c - 1 < re:
                    y = c - 1 - (re - (ul + c - 1))
                elif ul < re:
                    y = re - ul
                    d = 2
                else:
                    y -= re
        if data[x][y][1] != -1:
            if sarks[data[x][y][1]][5] < z:
                sarks[data[x][y][1]][0] = 1
                data[x][y][1] = j
                sarks[j] = [a, x, y, s, d, z]
            else:
                sarks[j][0] = 1
        else:
            data[x][y][1] = j
            sarks[j] = [a, x, y, s, d, z]
    for nx in range(r):
        for ny in range(c):
            data[nx][ny][0] = data[nx][ny][1]
            data[nx][ny][1] = -1
print(res)
