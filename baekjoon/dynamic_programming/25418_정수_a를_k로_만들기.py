n, m = map(int, input().split())
dp = [1e10] * (m + 1)
dp[m] = 0
for i in range(m, n - 1, -1):
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    if i % 2 == 0:
        dp[i // 2] = min(dp[i // 2], dp[i] + 1)
print(dp[n])
