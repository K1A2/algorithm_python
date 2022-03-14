def comb(n, depth, to_depth, num, numbers, result, visited):
    if to_depth == depth:
        result.add(int(num))
        return result
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            result = comb(n, depth + 1, to_depth, num + numbers[i], numbers, result, visited)
            visited[i] = 0
    return result

def solution(numbers):
    answer = 0
    c = set()
    visited = [0] * len(numbers)
    for i in range(1, len(numbers) + 1):
        c = comb(len(numbers), 0, i, '', numbers, c, visited)
    for i in c:
        if i <= 1:
            continue
        isp = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                isp = False
                break
        if isp:
            answer += 1
    return answer

print(solution('17'))
print(solution('011'))