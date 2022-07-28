import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
data = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
data = [(0, 0)] + data
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = data[i]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
print(dp[n][k])
