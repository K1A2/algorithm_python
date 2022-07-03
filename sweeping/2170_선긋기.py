import sys
input = sys.stdin.readline
n = int(input().rstrip())
lines = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
lines.sort()

res = 0
m = int(-1 * 1e10)
for l, r in lines:
    if l >= m:
        res += r - l
        m = r
    else:
        if r > m:
            res += r - m
            m = r
print(res)
