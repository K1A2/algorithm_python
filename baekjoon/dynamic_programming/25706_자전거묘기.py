import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[-1] = 1
for i in range(n - 2, -1, -1):
    new_idx = i + 1 + data[i]
    if new_idx < n:
        dp[i] = dp[new_idx] + 1
    else:
        dp[i] = dp[-1]
print(*dp)
