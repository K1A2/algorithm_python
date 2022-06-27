import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
datas = list(map(int, input().rstrip().split()))
datas.sort()

def backtracking(to, result, l, nums, m):
    if len(l) == m:
        result.append(tuple(l))
        return result
    for i in range(to):
        if i in l:
            continue
        l.append(i)
        result = backtracking(to, result, l, nums, m)
        l.pop()
    return result
result = [tuple([datas[j] for j in i]) for i in backtracking(len(datas), [], [], datas, m)]
result = list(set(result))
result.sort()
for i in result:
    print(*i)
