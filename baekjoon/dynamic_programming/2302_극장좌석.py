n = int(input())
vip = [int(input()) for _ in range(int(input()))] + [n + 1]
prev = 1
dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
ans = 1
for v in vip:
    r = v - prev
    prev = v + 1
    for i in range(3, r + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    ans *= dp[r]
print(ans)
