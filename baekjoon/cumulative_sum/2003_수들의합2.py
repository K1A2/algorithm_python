import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = list(map(int, input().split()))
for i in range(1, n):
    data[i] += data[i - 1]
ans = 0
for start in range(0, n):
    for end in range(0, start + 1):
        v = data[start]
        if end > 0:
            v -= data[end - 1]
        if v == m:
            ans += 1
print(ans)
