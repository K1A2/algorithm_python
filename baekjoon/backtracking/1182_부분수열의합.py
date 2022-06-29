import sys
input = sys.stdin.readline
n, s = map(int, input().rstrip().split())
data = list(map(int, input().rstrip().split()))

def backtracking(start, s_num, result, comb, count):
    if count == comb:
        if s_num == s:
            return result + 1
        else: return result
    for i in range(start, n):
        result = backtracking(i + 1, s_num + data[i], result, comb, count + 1)
    return result
res = 0
for i in range(1, n + 1):
    res += backtracking(0, 0, 0, i, 0)
print(res)