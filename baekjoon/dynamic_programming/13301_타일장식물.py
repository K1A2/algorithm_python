n = int(input())
if n == 1:
    print(4)
    exit()
dp = [0] * (n + 1)
dp[1] = 4
dp[2] = 6
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
