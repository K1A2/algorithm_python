import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = list(map(int, input().split()))
for i in range(1, n):
    data[i] += data[i - 1]
ans = data[m - 1]
for i in range(m, n):
    v = data[i] - data[i - m]
    ans = max(ans, v)
print(ans)
