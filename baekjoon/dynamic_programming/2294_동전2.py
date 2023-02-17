import sys
INF = 1e9
input = sys.stdin.readline
n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()
dp = [INF] * (m + 1)
dp[0] = 0
for i in data:
    if i > m:
        break
    for j in range(i, m + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[-1] if dp[-1] != INF else -1)
