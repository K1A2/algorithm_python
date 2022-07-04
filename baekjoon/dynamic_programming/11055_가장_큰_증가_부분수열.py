import sys
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
dp = data[:]
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + data[i])
print(max(dp))
