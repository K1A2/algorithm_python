n, k = map(int, input().split())
dp = [[1] * 31 for _ in range(31)]
if n <= 2 or n == k or k == 1:
    print(1)
    exit()
for i in range(3, n + 1):
    for j in range(2, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        if i == n and j == k:
            print(dp[i][j])
            exit()
