def solution(n, lost, reserve):
    cloth = [1 for _ in range(n)]
    check = [False for _ in range(n)]
    for i in range(n):
        if i + 1 in lost:
            cloth[i] -= 1
        elif i + 1 in reserve:
            cloth[i] += 1

    for i in range(n):
        count = cloth[i]
        if count == 1:
            check[i] = True
        elif count == 2:
            prev = i - 1
            next = i + 1
            if prev >= 0 and not check[prev]:
                if cloth[prev] == 0:
                    cloth[prev] += 1
                    cloth[i] -= 1
                    check[prev] = True
                else:
                    if next < len(check) and not check[next]:
                        if cloth[next] == 0:
                            cloth[next] += 1
                            cloth[i] -= 1
                        check[next] = True
            elif next < len(check) and not check[next]:
                if cloth[next] == 0:
                    cloth[next] += 1
                    cloth[i] -= 1
                check[next] = True
            check[i] = True
    return len(cloth) - cloth.count(0)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2