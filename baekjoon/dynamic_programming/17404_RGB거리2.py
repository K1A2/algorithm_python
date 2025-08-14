import sys
input = sys.stdin.readline
INF = int(1e10)
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = INF
for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][i] = data[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + data[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + data[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + data[j][2]
    dp[-1][i] = INF
    ans = min(min(dp[-1]), ans)
print(ans)
