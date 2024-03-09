import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = [1e10] * n
dp[0] = 0
for i in range(n):
    for j in range(data[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[-1] if dp[-1] != 1e10 else -1)
