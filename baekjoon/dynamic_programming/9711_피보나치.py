import sys
input = sys.stdin.readline
dp = [0] * 10001
dp[1] = 1
for i in range(2, 10001):
    dp[i] = dp[i-1] + dp[i-2]
for index in range(int(input())):
    p, q = map(int, input().split())
    print(f'Case #{index + 1}: {dp[p] % q}')
