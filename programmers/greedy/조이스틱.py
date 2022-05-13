def solution(name):
    answer = 0
    name = list(name)
    n = len(name)
    for i in range(n):
        diff = ord(name[i]) - ord('A')
        answer += min(diff, 26 - diff)

    return answer

print(solution("JEROEN"))
print(solution("JAN"))

def solution(S, K):
    m = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    now_idx = m.index(S)
    K %= 7
    return m[now_idx + K if now_idx + K < 7 else 7 - (now_idx + K)]
print(solution('Sat', 23))