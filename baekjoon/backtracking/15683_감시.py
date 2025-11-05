n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
pos = []
ans_max = n * m
for i in range(n):
    for j in range(m):
        if 1 <= data[i][j] <= 5:
            ans_max -= 1
            pos.append((i, j))
        elif data[i][j] == 6:
            ans_max -= 1

dxy = (
    (
        ((0, 1),),
        ((0, -1),),
        ((1, 0),),
        ((-1, 0),)
    ),
    (
        ((0, 1), (0, -1)),
        ((1, 0), (-1, 0))
    ),
    (
        ((-1, 0), (0, 1)),
        ((0, 1), (1, 0)),
        ((1, 0), (0, -1)),
        ((0, -1), (-1, 0))
    ),
    (
        ((0, -1), (-1, 0), (0, 1)),
        ((-1, 0), (0, 1), (1, 0)),
        ((0, 1), (1, 0), (0, -1)),
        ((1, 0), (0, -1), (-1, 0))
    ),
    (
        ((0, 1), (1, 0), (0, -1), (-1, 0)),
    )
)

ans = ans_max
block = n * m - ans_max

def backtracking(pos_idx, count):
    global ans
    if pos_idx == len(pos):
        ans = min(ans, ans_max - count)
        return
    px, py = pos[pos_idx]
    for i in dxy[data[px][py] - 1]:
        changed = []
        for d in i:
            x = px
            y = py
            while 1:
                x += d[0]
                y += d[1]
                if not (0 <= x < n and 0 <= y < m):
                    break
                if data[x][y] == 0:
                    data[x][y] = 1
                    count += 1
                    changed.append((x, y))
                elif 1 <= data[x][y] <= 5:
                    continue
                else:
                    break

        backtracking(pos_idx + 1, count)

        for c in changed:
            data[c[0]][c[1]] = 0
            count -= 1

backtracking(0, 0)
print(ans)
