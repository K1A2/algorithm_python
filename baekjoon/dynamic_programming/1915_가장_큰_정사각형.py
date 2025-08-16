n, m = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = 0
for i in range(n):
    dp[i][0] = data[i][0]
    ans = max(dp[i][0], ans)
for i in range(m):
    dp[0][i] = data[0][i]
    ans = max(dp[0][i], ans)
for i in range(1, n):
    for j in range(1, m):
        if data[i][j] == 0: continue
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + data[i][j]
        ans = max(dp[i][j], ans)
print(ans * ans)
