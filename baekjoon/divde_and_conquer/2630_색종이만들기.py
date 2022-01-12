import sys
n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
def find(xs, xe, ys, ye, w, b):
    if xe - xs == 1 and ye - ys == 1:
        if data[xs][ys]:
            b += 1
        else:
            w += 1
        return w, b
    else:
        all_white = all_blue = False
        for i in range(xs, xe):
            for j in range(ys, ye):
                if data[i][j]:
                    all_blue = True
                else:
                    all_white = True
        if all_white and not all_blue:
            w += 1
        elif not all_white and all_blue:
            b += 1
        else:
            part = ((xs, xs + (xe - xs) // 2, ys, ys + (ye - ys) // 2), (xs, xs + (xe - xs) // 2, ys + (ye - ys) // 2, ye),
                    (xs + (xe - xs) // 2, xe, ys, ys + (ye - ys) // 2), (xs + (xe - xs) // 2, xe, ys + (ye - ys) // 2, ye))
            for i in part:
                w, b = find(i[0], i[1], i[2], i[3], w, b)
        return w, b
print('\n'.join([str(i) for i in find(0, n, 0, n, 0, 0)]))