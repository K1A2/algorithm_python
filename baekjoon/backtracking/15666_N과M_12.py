n, m = map(int, input().split())
datas = sorted(map(int, input().split()))
def backtracking(results, now, min_idx):
    if len(now) == m:
        res = ' '.join(map(str, now))
        if res not in results:
            results.append(res)
        return results
    for i in range(min_idx, n):
        now.append(datas[i])
        results = backtracking(results, now, i)
        now.pop()
    return results
print('\n'.join(backtracking([], [], 0)))
