a = int(input())
dp = [0] * 100001
dp[1] = dp[2] = 2
for i in range(3, a + 1):
    dp[i] = (dp[i - 2] * 2) % 16769023
print(dp[a])