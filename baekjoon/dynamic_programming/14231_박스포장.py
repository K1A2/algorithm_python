n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    max_value = 0
    for j in range(i):
        if data[j] < data[i] and max_value < dp[j]:
            max_value = dp[j]
    dp[i] = max_value + 1
print(max(dp))
