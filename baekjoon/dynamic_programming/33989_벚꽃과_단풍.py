n = int(input())
data = list(input().rstrip())
dp = [[0, 0] for _ in range(100001)]  # 이전에 단풍 있음/없음

for i in range(n):
    if data[i] == 'D':
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1] + 1
    else:
        dp[i + 1][0] = min(dp[i][1], dp[i][0] + 1)
        dp[i + 1][1] = dp[i][1]
print(min(dp[n]))
