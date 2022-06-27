def backtracking(to, result):
    if len(result) == to - 1:
        print(*result)
        return
    for i in range(1, to):
        if i in result:
            continue
        result.append(i)
        backtracking(to, result)
        result.pop()
backtracking(int(input()) + 1, [])