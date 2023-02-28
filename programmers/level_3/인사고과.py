def solution(scores):
    answer = 1
    target = scores[0]
    target_score = sum(scores[0])
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))

    max_score = 0
    for s in scores:
        if target[0] < s[0] and target[1] < s[1]:
            return -1
        if max_score <= s[1]:
            if target_score < sum(s):
                answer += 1
            max_score = s[1]
    return answer

testcase = [
    ([[2,2],[1,4],[3,2],[3,2],[2,1]], 4)
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(t[0]) == t[1]}')