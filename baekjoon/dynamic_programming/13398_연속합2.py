n = int(input())
data = list(map(int, input().split()))
dp = [[data[i]] * 2 for i in range(n)]
ans = max(dp[0])
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + data[i], data[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + data[i])
    ans = max(dp[i][0], dp[i][1], ans)
print(ans)
