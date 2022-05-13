def solution(s):
    if len(s) == 1:
        return 1
    answer = 10000
    for i in range(len(s) // 2, 0, -1):
        now = s[:i]
        count = 1
        n_str = ''
        is_added = False
        for j in range(i, len(s), i):
            if j + i > len(s):
                is_added = True
                n_str += (str(count) if count > 1 else '') + now + s[j:j + i]
                break
            if now == s[j:j + i]:
                count += 1
            else:
                n_str += (str(count) if count > 1 else '') + now
                count = 1
                now = s[j:j + i]
        if not is_added:
            n_str += (str(count) if count > 1 else '') + now
        answer = min(answer, len(n_str))
    return answer

print(solution('aabbaccc') == 7)
print(solution('ababcdcdababcdcd') == 9)
print(solution('abcabcdede') == 8)
print(solution('abcabcabcabcdededededede') == 14)
print(solution('xababcdcdababcdcd') == 17)