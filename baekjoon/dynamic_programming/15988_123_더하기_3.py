import sys
input = sys.stdin.readline
dp = [1, 2, 4]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n):
        dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009)
    print(dp[n - 1])