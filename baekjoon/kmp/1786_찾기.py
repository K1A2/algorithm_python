import sys
a = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
def get_pi():
    m = len(pattern)
    lps = [0] * m
    idx = 0
    for i in range(1, m):
        while idx > 0 and pattern[i] != pattern[idx]:
            idx = lps[idx - 1]
        if pattern[i] == pattern[idx]:
            idx += 1
            lps[i] = idx
    return lps
def kmp():
    n = len(a)
    m = len(pattern)
    lps = get_pi()
    idx = count = 0
    idx_result = []
    for i in range(n):
        while idx > 0 and a[i] != pattern[idx]:
            idx = lps[idx - 1]
        if a[i] == pattern[idx]:
            if idx == m - 1:
                count += 1
                idx_result.append(i - idx + 1)
                idx = lps[idx]
            else:
                idx += 1
    return count, idx_result
res = kmp()
print(f'{res[0]}')
print(*res[1])