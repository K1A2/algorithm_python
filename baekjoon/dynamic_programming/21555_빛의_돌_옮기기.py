n, k = map(int, input().split())
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = d1[0]
dp[0][1] = d2[0]
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0] + d1[i], dp[i - 1][1] + d1[i] + k)
    dp[i][1] = min(dp[i - 1][1] + d2[i], dp[i - 1][0] + d2[i] + k)
print(min(dp[-1]))
