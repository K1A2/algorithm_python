import sys
n, m, b = map(int, sys.stdin.readline().rstrip().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
a = []
result = []
for i in data: a += i
for i in range(min(a), max(a) + 1):
    sec = 0
    b_save = b
    for j in data:
        for k in j:
            if i > k:
                sec += i - k
                b_save -= i - k
            elif i < k:
                sec += (k - i) * 2
                b_save += k - i
    if b_save >= 0:
        result.append((sec, i))
result = sorted(result, key=lambda a:a[0])
now = result[0]
for i in range(1, len(result)):
    if now[0] != result[i][0]:
        break
    if now[1] < result[i][1]:
        now = result[i]
print(' '.join([str(i) for i in now]))