import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
dxy = ((0, 1), (1, 0))
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[-1][-1])
            exit()
        if j + data[i][j] < n:
            dp[i][j + data[i][j]] += dp[i][j]
        if i + data[i][j] < n:
            dp[i + data[i][j]][j] += dp[i][j]
