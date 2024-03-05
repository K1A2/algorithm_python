import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    if board[0][i] == 1:
        break
    dp[0][i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        if board[i][j] == 0 and board[i - 1][j] == 0 and board[i][j - 1] == 0:
            dp[i][j][2] = sum(dp[i - 1][j - 1])
        if board[i][j] == 0 and board[i][j - 1] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        if board[i][j] == 0 and board[i - 1][j] == 0:
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
print(sum(dp[-1][-1]))
