dp = [[0] * 64 for _ in range(10)]
sdp = [0] * 64
sdp[0] = 10
for i in range(64):
    dp[0][i] = 1
for i in range(10):
    dp[i][0] = 1
last = 0
for _ in range(int(input())):
    n = int(input()) - 1
    if last >= n:
        print(sdp[n])
        continue
    for i in range(last + 1, n + 1):
        s = 1
        for j in range(1, 10):
            dp[j][i] = dp[j][i - 1] + dp[j - 1][i]
            s += dp[j][i]
        sdp[i] = s
    last = n
    print(sdp[n])
