import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [sys.stdin.readline().rstrip() for _ in range(n)]
for _ in range(m):
    i = sys.stdin.readline().rstrip()
    try:
        print(data[int(i) - 1])
    except:
        print(data.index(i) + 1)