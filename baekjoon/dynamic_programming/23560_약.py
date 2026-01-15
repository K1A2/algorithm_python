n = int(input())
dp = [0] * (n + 1)
dp[1] = 2
for i in range(2, n + 1):
    dp[i] = dp[i - 1] * 3
print(dp[n])
