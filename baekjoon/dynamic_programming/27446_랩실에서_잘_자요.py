import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pages = sorted(list(set(map(int, input().split()))))
target = []
s = 1
for i in pages:
    for j in range(s, i):
        target.append(j)
    s = i + 1
for i in range(s, n + 1):
    target.append(i)
page = ans = 0
for i in target:
    if page != 0:
        ans += min(7, 2 * (i - page))
    else:
        ans += 7
    page = i
print(ans)
