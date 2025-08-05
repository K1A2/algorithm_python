n = int(input())
data = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = data[i]
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[j] + dp[i - j])
print(dp[-1])
