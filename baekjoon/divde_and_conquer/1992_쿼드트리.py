import sys
n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
def find(xs, xe, ys, ye, result):
    if xe - xs == 1 and ye - ys == 1:
        if data[xs][ys]:
            result += '1'
        else:
            result += '0'
        return result
    else:
        all_white = all_blue = False
        for i in range(xs, xe):
            for j in range(ys, ye):
                if data[i][j]:
                    all_blue = True
                else:
                    all_white = True
        if all_white and not all_blue:
            result += '0'
        elif not all_white and all_blue:
            result += '1'
        else:
            result += '('
            part = ((xs, xs + (xe - xs) // 2, ys, ys + (ye - ys) // 2), (xs, xs + (xe - xs) // 2, ys + (ye - ys) // 2, ye),
                    (xs + (xe - xs) // 2, xe, ys, ys + (ye - ys) // 2), (xs + (xe - xs) // 2, xe, ys + (ye - ys) // 2, ye))
            for i in part:
                result = find(i[0], i[1], i[2], i[3], result)
            result += ')'
        return result
print(find(0, n, 0, n, ''))