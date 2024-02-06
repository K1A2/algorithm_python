n = int(input())
dp = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
print(dp[n][n], n ** 2)
