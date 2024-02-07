n = int(input())
dp = [0] * 1001
dp[1] = dp[3] = dp[4] = dp[5] = 1
dp[2] = 0
for i in range(6, n + 1):
    if dp[i - 1] == 0 or dp[i - 3] == 0 or dp[i - 4] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
if dp[n] == 1:
    print('SK')
else:
    print('CY')
