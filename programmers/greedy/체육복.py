def reserve_check(l, check):
    if 0 <= l < len(check):
        if not check[l]:
            return True
        else:
            return False
    else:
        return False


def solution(n, lost, reserve):
    cloth = [1 for _ in range(n)]
    check = [False for _ in range(n)]
    for i in range(n):
        if i + 1 in lost:
            cloth[i] -= 1
        if i + 1 in reserve:
            cloth[i] += 1
        if cloth[i] > 0:
            check[i] = True
        else:
            check[i] = False

    for i in range(len(cloth)):
        if cloth[i] == 2:
            prev, next = i - 1, i + 1
            if reserve_check(prev, check):
                cloth[prev] += 1
                cloth[i] -= 1
                check[prev] = True
            else:
                if reserve_check(next, check):
                    cloth[next] += 1
                    cloth[i] -= 1
                    check[next] = True

    return check.count(True)

print(solution(5, [2, 4], [1, 3, 5]) == 5) # 5
print(solution(5, [2, 4], [3]) == 4) # 4
print(solution(3, [3], [1]) == 2) # 2