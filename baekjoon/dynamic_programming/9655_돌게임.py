n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 1]) + 1
if dp[n] % 2 == 0:
    print('CY')
else:
    print('SK')