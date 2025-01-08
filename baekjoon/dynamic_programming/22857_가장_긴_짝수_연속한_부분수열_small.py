n, k = map(int, input().split())
data = [0] + list(map(int, input().split()))
dp = [[0] * (k + 1) for _ in range(n + 1)]
res = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        if data[i] % 2 == 0:
            dp[i][j] = dp[i - 1][j] + 1
        elif j > 0:
            dp[i][j] = dp[i - 1][j - 1]
        res = max(dp[i][j], res)
print(res)
