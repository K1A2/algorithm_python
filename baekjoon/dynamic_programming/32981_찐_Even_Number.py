dp = [0] * 10000001
dp[1] = 5
for i in range(2, 10000001):
    dp[i] = ((4 if i == 2 else 5) * dp[i - 1]) % (10 ** 9 + 7)
for _ in range(int(input())):
    print(dp[int(input())])
