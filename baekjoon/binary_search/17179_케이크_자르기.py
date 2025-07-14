import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
data = [int(input()) for _ in range(m)]
data.append(l)

def check(target, cut):
    count = 0
    last_cut = 0
    for i in range(m + 1):
        if data[i] - last_cut >= target:
            count += 1
            last_cut = data[i]
    return count > cut

for _ in range(n):
    c = int(input())
    low = 0
    high = l
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid, c):
            low = mid + 1
        else:
            high = mid - 1
    print(high)
