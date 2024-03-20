import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = data[:]
for i in range(1, n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], data[i] + dp[j])
print(max(dp))
