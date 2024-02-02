r, c, w = map(lambda x: int(x) - 1, input().split())
w += 1
n = r + w
dp = [[1] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1):
        if i >= 2 and 1 <= j < i:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        if r <= i < n and c <= j <= c + (i - r):
            ans += dp[i][j]
print(ans)
