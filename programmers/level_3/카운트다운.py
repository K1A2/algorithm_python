def solution(target):
    dp = [[target - i, target - i] for i in range(target + 1)]
    for i in range(target, -1, -1):
        for j in range(20, 0, -1):
            if i - 50 >= 0:
                if dp[i - 50][0] > dp[i][0] + 1:
                    dp[i - 50] = list(map(lambda x: x + 1, dp[i]))
                elif dp[i - 50][0] == dp[i][0] + 1 and dp[i - 50][1] < dp[i][1] + 1:
                    dp[i - 50][1] = dp[i][1] + 1
            if i - j >= 0:
                if dp[i - j][0] > dp[i][0] + 1:
                    dp[i - j] = list(map(lambda x: x + 1, dp[i]))
                elif dp[i - j][0] == dp[i][0] + 1 and dp[i - j][1] < dp[i][1] + 1:
                    dp[i - j][1] = dp[i][1] + 1
            if i - j * 2 >= 0:
                if dp[i - j * 2][0] > dp[i][0] + 1:
                    dp[i - j * 2] = [dp[i][0] + 1, dp[i][1]]
                elif dp[i - j * 2][0] == dp[i][0] + 1 and dp[i - j * 2][1] < dp[i][1]:
                    dp[i - j * 2][1] = dp[i][1]
            if i - j * 3 >= 0:
                if dp[i - j * 3][0] > dp[i][0] + 1:
                    dp[i - j * 3] = [dp[i][0] + 1, dp[i][1]]
                elif dp[i - j * 3][0] == dp[i][0] + 1 and dp[i - j * 3][1] < dp[i][1]:
                    dp[i - j * 3][1] = dp[i][1]
    return dp[0]

testcase = [
    ([21], [1,0]),
    ([58], [2,2]),
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(*t[0]) == t[-1]}')