n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    for left in range(n - i):
        right = left + i
        dp[left][right] = 2**31
        for k in range(left, right):
            dp[left][right] = min(dp[left][right], dp[left][k] + dp[k + 1][right] + data[left][0] * data[k][1] * data[right][1])
print(dp[0][-1])
