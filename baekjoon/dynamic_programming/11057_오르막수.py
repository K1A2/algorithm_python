n = int(input())
dp = [[0] * 10 for _ in range(n)]
for i in range(10): dp[0][i] = 1
for x in range(1, n):
    for y in range(10):
        if not y:
            dp[x][y] = sum(dp[x - 1]) % 10007
        else:
            dp[x][y] = (dp[x][y - 1] - dp[x - 1][y - 1])  % 10007
print(sum(dp[n - 1])  % 10007)