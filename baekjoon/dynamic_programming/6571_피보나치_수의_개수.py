import sys
input = sys.stdin.readline
n = 480
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    min_idx = max_idx = 0
    for i in range(1, n):
        if dp[i - 1] < a <= dp[i]:
            min_idx = i
        if dp[i - 1] <= b < dp[i]:
            max_idx = i
    print(max_idx - min_idx)
