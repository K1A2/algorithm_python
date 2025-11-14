import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

shell = []
for i in range(min(n // 2, m // 2)):
    dxy = [1, 0]
    x, y = i + dxy[0], i + dxy[1]
    s = [data[i][i]]
    while 1:
        if x == n - i - 1 and y == i:
            dxy = [0, 1]
        elif x == n - i - 1 and y == m - i - 1:
            dxy = [-1, 0]
        elif x == i and y == m - i - 1:
            dxy = [0, -1]
        elif x == y == i:
            break
        s.append(data[x][y])

        x += dxy[0]
        y += dxy[1]
    shell.append(s)

new_shell = []
for s in shell:
    l = len(s)
    move = r % l
    new_l = [0] * l
    for i in range(l):
        new_l[i] = s[i - move]
    new_shell.append(new_l)

for _ in range(r):
    pos_x = 0
    for i in range(min(n // 2, m // 2)):
        dxy = [1, 0]
        x = y = i
        pos_y = 0
        while pos_y < len(new_shell[pos_x]):
            data[x][y] = new_shell[pos_x][pos_y]

            if x == n - i - 1 and y == i:
                dxy = [0, 1]
            elif x == n - i - 1 and y == m - i - 1:
                dxy = [-1, 0]
            elif x == i and y == m - i - 1:
                dxy = [0, -1]

            x += dxy[0]
            y += dxy[1]
            pos_y += 1
        pos_x += 1
for d in data:
    sys.stdout.write(' '.join(map(str, d)) + '\n')
