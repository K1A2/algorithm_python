n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i // 2] + dp[i - (i // 2)] + (i // 2 * (i - (i // 2)))
print(dp[-1])
