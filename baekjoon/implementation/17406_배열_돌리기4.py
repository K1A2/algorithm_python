import sys
input= sys.stdin.readline
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
rcs = [list(map(int, input().split())) for _ in range(k)]
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
def change(dir, rcs):
    r, c, s = rcs
    r -= 1
    c -= 1
    for now_s in range(s):
        lx, ly, rx, ry = r - s + now_s, c - s + now_s, r + s - now_s, c + s - now_s
        d_idx = 0
        x, y = lx, ly + 1
        if dir == -1: y = ry - 1
        save = data[x][y]
        is_last = 0
        while 1:
            if (x == lx or x == rx) and (y == ly or y == ry):
                d_idx += dir
                if d_idx > 3 or d_idx < -3:
                    d_idx = 0
                    is_last = 1
            x, y = x + dir * dxy[d_idx][0], y + dir * dxy[d_idx][1]
            save, data[x][y] = data[x][y], save
            if is_last: break
def backtracking(result, used):
    if len(used) == k:
        for d in data:
            result = min(result, sum(d))
        return result
    for i in range(k):
        if i in used:
            continue
        change(1, rcs[i])
        used.append(i)
        result = backtracking(result, used)
        used.pop()
        change(-1, rcs[i])
    return result
print(backtracking(1000 * 50 + 1, []))
