def findA(s, start):
    count = 0
    for i in range(start, len(s)):
        if start[i] == 'A':
            count += 1
        else:
            break
    if count > s + 1:
        return True
    else:
        return False

def solution(name):
    is_gone = [False for _ in range(len(name))]
    alphabet = ['A' for _ in range(len(name))]

    cursor = 0
    count = 0
    direction = 1
    while alphabet != name:
        now_al, now_na = alphabet[cursor], name[cursor]
        count += ord(now_na) - ord('A')
        alphabet[cursor] = now_na
        is_gone[cursor] = True

        check = cursor + direction
        if check >= len(name):
            check = 0
        elif check < 0:
            check = len(name) - 1

    answer = 0
    return answer

print(solution("JEROEN") == 56)
print(solution("JAN") == 23)