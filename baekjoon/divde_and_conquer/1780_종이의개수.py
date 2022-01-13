import sys
n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
def find(xs, xe, ys, ye, w, b, r):
    if xe - xs == 1 and ye - ys == 1:
        if data[xs][ys] == -1:
            b += 1
        elif data[xs][ys] == 0:
            w += 1
        else:
            r += 1
        return b, w, r
    else:
        all_white = all_blue = all_red = False
        for i in range(xs, xe):
            for j in range(ys, ye):
                if data[i][j] == -1:
                    all_blue = True
                elif data[i][j] == 0:
                    all_white = True
                else:
                    all_red = True
        if all_white and not all_blue and not all_red:
            w += 1
        elif not all_white and all_blue and not all_red:
            b += 1
        elif not all_white and not all_blue and all_red:
            r += 1
        else:
            x_gap = (xe - xs) // 3
            y_gap = (ye - ys) // 3
            part = ((xs, xs + x_gap, ys, ys + y_gap),
                    (xs, xs + x_gap, ys + y_gap, ys + y_gap * 2),
                    (xs, xs + x_gap, ys + y_gap * 2, ye),
                    (xs + x_gap, xs + x_gap * 2, ys, ys + y_gap),
                    (xs + x_gap, xs + x_gap * 2, ys + y_gap, ys + y_gap * 2),
                    (xs + x_gap, xs + x_gap * 2, ys + y_gap * 2, ye),
                    (xs + x_gap * 2, xe, ys, ys + y_gap),
                    (xs + x_gap * 2, xe, ys + y_gap, ys + y_gap * 2),
                    (xs + x_gap * 2, xe, ys + y_gap * 2, ye))
            for i in part:
                b, w, r = find(i[0], i[1], i[2], i[3], w, b, r)
        return b, w, r
print('\n'.join([str(i) for i in find(0, n, 0, n, 0, 0, 0)]))