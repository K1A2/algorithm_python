for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    accum = [0] * (n + 1)
    for i in range(n):
        accum[i + 1] = accum[i] + data[i]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n):
        for left in range(1, n - i + 1):
            right = left + i
            dp[left][right] = min([dp[left][mid] + dp[mid + 1][right] for mid in range(left, right)]) + accum[right] - accum[left - 1]
    print(dp[1][n])
