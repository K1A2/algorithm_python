import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
dp[0] = data[0][2]
for i in range(1, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i][2])
print(dp[n - 1])
