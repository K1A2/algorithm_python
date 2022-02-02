import sys
from itertools import combinations
n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
a = [0] * n
asw = 1e10
def backtracking(count, s):
    global asw
    if count == 0:
        a_num = []
        b_num = []
        for i in range(n):
            if a[i]:
                a_num.append(i)
            else:
                b_num.append(i)
        a_s = b_s = 0
        for i in combinations(a_num, 2):
            a_s += data[i[0]][i[1]] + data[i[1]][i[0]]
        for i in combinations(b_num, 2):
            b_s += data[i[0]][i[1]] + data[i[1]][i[0]]
        asw = min(asw, abs(a_s - b_s))
    for i in range(s, n):
        a[i] = 1
        backtracking(count - 1, i + 1)
        a[i] = 0
backtracking(n // 2, 0)
print(asw)