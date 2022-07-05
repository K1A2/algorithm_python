import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
set_n = set([input().rstrip() for _ in range(n)])
count = 0
for i in range(m):
    if input().rstrip() in set_n:
        count += 1
print(count)
