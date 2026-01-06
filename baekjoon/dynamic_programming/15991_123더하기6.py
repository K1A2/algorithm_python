import sys
input = sys.stdin.readline
dp = [0] * 100001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
last = 4
for _ in range(int(input())):
    n = int(input())
    for i in range(last, n + 1):
        dp[i] = (dp[i - 6] + dp[i - 4] + dp[i - 2]) % 1000000009
    if last < n: last = n
    print(dp[n])
