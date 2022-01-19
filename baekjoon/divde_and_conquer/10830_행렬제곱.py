import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
def gop(a, b):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result
def cal(n, m):
    if n == 1:
        return data
    b = cal(n // 2, m)
    if n % 2 == 0:
        return gop(b, b)
    else:
        return gop(gop(b, b), m)
result = [[j % 1000 for j in i] for i in cal(m, data)]
for i in result:
    print(' '.join([str(j) for j in i]))