count = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
char_to_int = lambda x: [count[ord(i) - ord('A')] for i in x]
a, b = char_to_int(input()), char_to_int(input())
dp = [[0 for i in range(2 * len(a))] for j in range(2 * len(a) - 1)]

for i in range(len(a) + 1):
    if i != len(a):
        dp[0][i * 2] = a[i]
    if i != 0:
        dp[0][i * 2 - 1] = b[i - 1]

for i in range(1, 2 * len(a) - 1):
    for j in range(2 * len(a) - i):
        dp[i][j] = int(str(dp[i-1][j] + dp[i-1][j+1])[-1])

print(dp[-1][0], dp[-1][1], sep='')
