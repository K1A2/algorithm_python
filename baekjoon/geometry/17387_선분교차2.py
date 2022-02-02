import sys
ax, ay, bx, by = map(int, sys.stdin.readline().rstrip().split())
cx, cy, dx, dy = map(int, sys.stdin.readline().rstrip().split())
def ccw(ax, ay, bx, by, cx, cy):
    res = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if res < 0:
        return -1
    elif res > 0:
        return 1
    else:
        return 0
asw = 0
if ccw(ax, ay, bx, by, cx, cy) * ccw(ax, ay, bx, by, dx, dy) == 0 and ccw(cx, cy, dx, dy, ax, ay) * ccw(cx, cy, dx, dy, bx, by) == 0:
    if min(ax, bx) <= max(cx, dx) and max(ax, bx) >= min(cx, dx) and min(ay, by) <= max(cy, dy) and min(cy, dy) <= max(ay, by):
        asw = 1
elif ccw(ax, ay, bx, by, cx, cy) * ccw(ax, ay, bx, by, dx, dy) <= 0 and ccw(cx, cy, dx, dy, ax, ay) * ccw(cx, cy, dx, dy, bx, by) <= 0:
    asw = 1
print(asw)