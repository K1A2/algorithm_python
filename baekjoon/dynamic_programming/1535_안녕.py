import sys
input = sys.stdin.readline
n = int(input())
hp = list(map(int, input().split()))
pleasure = list(map(int, input().split()))
dp = [[0] * 100 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, 100):
        if j < hp[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i - 1]] + pleasure[i - 1])
print(dp[-1][-1])
