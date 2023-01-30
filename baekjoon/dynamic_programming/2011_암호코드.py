data = list(map(int, list(input())))
n = len(data)
dp = [0] * (n + 1)
if data[0] == 0:
    print(0)
    exit()
dp[0] = dp[1] = 1
data = [0] + data
for i in range(2, n + 1):
    if data[i] != 0:
        dp[i] += dp[i - 1]
    if 10 <= data[i - 1] * 10 + data[i] <= 26:
        dp[i] += dp[i - 2]
print(dp[n] % 1000000)
