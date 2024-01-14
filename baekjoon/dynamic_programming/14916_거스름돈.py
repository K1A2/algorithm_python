n = int(input())
dp = [0] * 100001
dp[0] = dp[1] = dp[3] = 100002
dp[2] = dp[5] = 1
dp[4] = 2
for i in range(6, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1
print(dp[n] if dp[n] <= 100000 else -1)
