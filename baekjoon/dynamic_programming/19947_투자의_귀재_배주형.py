m, y = map(int, input().split())
dp = [0] * (y + 1)
dp[0] = m
for i in range(1, y + 1):
    l = []
    if i - 1 >= 0:
        l.append(int(dp[i - 1] * 1.05))
    if i - 3 >= 0:
        l.append(int(dp[i - 3] * 1.2))
    if i - 5 >= 0:
        l.append(int(dp[i - 5] * 1.35))
    dp[i] = max(l)
print(dp[y])
