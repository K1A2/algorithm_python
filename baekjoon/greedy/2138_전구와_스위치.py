import sys
input = sys.stdin.readline
n = int(input())
a, b = list(input().rstrip()), list(input().rstrip())
def count(start_idx):
    data = [int(a[i] != b[i]) for i in range(n)]
    res = 0
    for i in range(start_idx, n):
        if not i or data[i - 1]:
            data[i] = 1 - data[i]
            if i - 1 >= 0: data[i - 1] = 1 - data[i - 1]
            if i + 1 < n: data[i + 1] = 1 - data[i + 1]
            res += 1
    if sum(data):
        res = -1
    return res
z, o = count(0), count(1)
if z == -1 and o == -1:
    print(-1)
elif o != -1:
    print(o)
elif z != -1:
    print(z)
else:
    print(min(o, z))
