def solution(target):
    dp = [[target - i, target - i] for i in range(target + 1)]
    for i in range(target, -1, -1):
        if i - 50 >= 0:
            if dp[i - 50][0] > dp[i][0] + 1:
                dp[i - 50] = list(map(lambda x: x + 1, dp[i]))
            elif dp[i - 50][0] == dp[i][0] + 1:
                dp[i - 50] = [dp[i - 50][0] + 1, max(dp[i][1], dp[i - 50][1]) + 1]
        for j in range(20, 0, -1):
            if i - j >= 0:
                if dp[i - j][0] > dp[i][0] + 1:
                    dp[i - j] = list(map(lambda x: x + 1, dp[i]))
                elif dp[i - j][0] == dp[i][0] + 1:
                    dp[i - j] = [dp[i - j][0] + 1, max(dp[i][1], dp[i - j][1]) + 1]
                else:
                    dp[i - j] =
    return dp[0]

testcase = [
    ([21], [1,0]),
    ([58], [2,2]),
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(*t[0]) == t[-1]}')