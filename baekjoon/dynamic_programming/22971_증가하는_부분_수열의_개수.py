n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    value = 0
    for j in range(i):
        if data[j] < data[i]:
            value += dp[j] % 998244353
    dp[i] = (value + 1) % 998244353
print(*dp)
