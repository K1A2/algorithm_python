import sys
input = sys.stdin.readline
data = list(map(int, list(input().rstrip())))
n = len(data)
dp = [[0] * 35 for _ in range(n)]
dp[0][data[0]] = 1
for i in range(1, n):
    for j in range(1, 35):
        if dp[i - 1][j]:
            if j * 10 + data[i] <= 34: dp[i][j * 10 + data[i]] += dp[i - 1][j]
            if 0 < data[i]: dp[i][data[i]] += dp[i - 1][j]
print(sum(dp[-1]))
