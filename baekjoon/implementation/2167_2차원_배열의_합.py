import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(1, m):
        data[i][j] += data[i][j - 1]
for _ in range(int(input())):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, input().split())
    res = 0
    for x in range(x1, x2 + 1):
        res += data[x][y2]
        if y1 > 0:
            res -= data[x][y1 - 1]
    print(res)
