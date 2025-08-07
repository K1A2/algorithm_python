n, s, m = map(int, input().split())
data = list(map(int, input().split()))
dp = [0] * (m + 1)
dp[s] = 1
for d in data:
    n_dp = [0] * (m + 1)
    c = 0
    for i in range(m + 1):
        if dp[i] == 0: continue
        c = 1
        if i - d >= 0:
            n_dp[i - d] = 1
        if i + d <= m:
            n_dp[i + d] = 1
    if c == 0:
        print(-1)
        exit()
    dp = n_dp
for i in range(m, -1, -1):
    if dp[i] == 1:
        print(i)
        exit()
print(-1)
