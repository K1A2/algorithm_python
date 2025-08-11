INF = 1e10
n = int(input())
road = list(input().rstrip())
dp = [INF] * n
dp[0] = 0
for i in range(n):
    t = road[i]
    if dp[i] >= INF: continue
    for j in range(i + 1, n):
        if (t == 'B' and road[j] != 'O') or (t == 'O' and road[j] != 'J') or (t == 'J' and road[j] != 'B'):
            continue
        dp[j] = min(dp[j], dp[i] + (j - i) * (j - i))
print(dp[-1] if dp[-1] < INF else -1)
