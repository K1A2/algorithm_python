n, m = map(int, input().split())
dp = [0] * 10000
for i in range(m):
    dp[i] = 1
    if i == m - 1:
        dp[i] = 2
for i in range(m, n):
    dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007
print(dp[n - 1])
