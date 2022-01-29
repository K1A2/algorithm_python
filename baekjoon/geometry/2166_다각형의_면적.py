import sys
import math
dots = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
dots.reverse()
x = y = 0
for i in range(len(dots) - 1):
    x += dots[i][0] * dots[i + 1][1]
    y += dots[i + 1][0] * dots[i][1]
x += dots[len(dots) - 1][0] * dots[0][1]
y += dots[0][0] * dots[len(dots) - 1][1]
print(math.fabs(round((x - y) / 2, 1)))