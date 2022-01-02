import math
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        line = math.fabs((2 * (x1 - x2)) * x1 + (2 * (y1 - y2)) * y1 + - 1 * (r2 ** 2 - r1 ** 2 + x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2)) / math.sqrt((2 * (x1 - x2)) ** 2 + (2 * (y1 - y2)) ** 2)
        if line < r1:
            print(2)
        elif line == r1:
            print(1)
        else:
            print(0)