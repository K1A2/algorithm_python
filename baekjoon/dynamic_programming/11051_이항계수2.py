a, b = map(int, input().split())
dp = [[1] * (b + 1) for _ in range(a + 1)]
for i in range(1, b + 1):
    for j in range(i + 1, a + 1):
        dp[j][i] = (dp[j - 1][i - 1] + dp[j - 1][i]) % 10007
print(dp[-1][-1])
