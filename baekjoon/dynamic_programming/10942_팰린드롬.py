import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for s in range(n - i):
        e = s + i
        if s == e:
            dp[s][e] = 1
        elif data[s] == data[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1]: dp[s][e] = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])
