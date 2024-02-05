n = int(input())
dp1, dp2 = 1, 1
for i in range(n - 2):
    dp1, dp2 = dp2, (dp1 + dp2) % 1000000007
print(dp2, n - 2)
