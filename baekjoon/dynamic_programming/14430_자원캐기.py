import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        maximum = data[i][j]
        if i > 0:
            maximum = max(maximum, dp[i - 1][j] + data[i][j])
        if j > 0:
            maximum = max(maximum, dp[i][j - 1] + data[i][j])
        dp[i][j] = maximum
print(dp[-1][-1])
