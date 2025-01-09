n = int(input())
dp = [0] * 21
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for i in range(5, n + 1):
    if i % 2 == 0:
        dp[i] = dp[i - 1] * 2 - dp[i - 4] - dp[i - 5]
    else:
        dp[i] = dp[i - 1] * 2
print(dp[n])
