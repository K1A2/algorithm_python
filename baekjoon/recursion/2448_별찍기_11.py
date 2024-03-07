total = int(input())

def recursion(n):
    if n == 3:
        return ['*', '* *', '*****']
    tmp = recursion(n // 2)
    res = [i for i in tmp]
    for idx, i in enumerate(range(n // 2 + 1, n + 1)):
        res.append(tmp[idx] + ' ' * (n - 1 - 2 * idx) + tmp[idx])
    return res


for idx, i in enumerate(recursion(total)):
    print(' ' * (total - idx - 1) + i + ' ' * (total - idx - 1))
