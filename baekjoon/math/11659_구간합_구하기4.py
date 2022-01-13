import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0]
for i in data:
    d.append(d[-1] + i)
data = d
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(data[b] - data[a - 1])