n, m, k = map(int, input().split())
if k % m == 0:
    r = (k // m - 1, m - 1)
else:
    r = (k // m, k % m - 1)
if k == 0:
    r = (n - 1, m - 1)
dp = [[0] * m for _ in range(n)]
for i in range(r[0] + 1):
    for j in range(r[1] + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
for i in range(r[0], n):
    for j in range(r[1], m):
        if i == r[0] and j == r[1]:
            continue
        if i == r[0] or j == r[1]:
            dp[i][j] = dp[r[0]][r[1]]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[-1][-1])
