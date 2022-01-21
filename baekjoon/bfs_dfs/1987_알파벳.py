import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
check = {data[0][0]}
result = 1
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def find(x, y, check, count):
    global result
    finish = True
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] not in check:
            check.add(data[nx][ny])
            find(nx, ny, check, count + 1)
            check.remove(data[nx][ny])
            finish = False
    if finish:
        if result < count + 1:
            result = count + 1
find(0, 0, check, 0)
print(result)