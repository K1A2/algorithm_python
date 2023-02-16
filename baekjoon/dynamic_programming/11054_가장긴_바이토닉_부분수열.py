import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data = [data, data[::-1]]
dp = [[1] * n, [1] * n]

for i in range(n):
    for j in range(i):
        for k in range(2):
            if data[k][i] > data[k][j]:
                dp[k][i] = max(dp[k][i], dp[k][j] + 1)
result = [0] * n
for i in range(n):
    result[i] = dp[0][i] + dp[1][n - i - 1]
print(max(result) - 1)
