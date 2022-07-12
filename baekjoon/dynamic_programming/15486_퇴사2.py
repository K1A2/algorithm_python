import sys
n = int(sys.stdin.readline().rstrip())
t, p = [0] * (n + 1), [0] * (n + 1)
for i in range(n):
    t[i], p[i] = map(int, sys.stdin.readline().rstrip().split())
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])