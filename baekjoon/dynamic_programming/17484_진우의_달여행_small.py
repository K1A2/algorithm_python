import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i] = [data[0][i], data[0][i], data[0][i]]
for i in range(1, n):
    for j in range(m):
        left = mid = right = 1e10
        if j > 0:
            right = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + data[i][j]
        if j < m - 1:
            left = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + data[i][j]
        mid = min(dp[i - 1][j][0], dp[i - 1][j][2]) + data[i][j]
        dp[i][j] = [left, mid, right]
print(min([min(i) for i in dp[-1]]))
