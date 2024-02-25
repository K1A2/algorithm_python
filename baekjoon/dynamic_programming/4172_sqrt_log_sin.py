import math
import sys
input = sys.stdin.readline
dp = [0] * 1000001
dp[0] = 1
last = 1
while 1:
    n = int(input())
    if n == -1:
        break
    if last > n:
        print(dp[n])
        continue
    for i in range(last, n + 1):
        dp[i] = ((dp[math.floor(i - math.sqrt(i))]
                 + dp[math.floor(math.log(i))]
                 + dp[math.floor(i * (math.sin(i) ** 2))]) % 1000000)
    last = n + 1
    print(dp[n])
