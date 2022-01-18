import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [[0] for _ in range(n + 1)]
data[0] = [0] * (n + 1)
for i in range(1, n + 1):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    data[i].append(a[0])
    for j in range(1, n):
        data[i].append(data[i][j] + a[j])
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    right = sum([data[i][y2] for i in range(x1, x2 + 1)])
    if y1 - 1 > 0:
        left = sum([data[i][y1 - 1] for i in range(x1, x2 + 1)])
    else:
        left = -1
    if left != -1:
        print(right - left)
    else:
        print(right)