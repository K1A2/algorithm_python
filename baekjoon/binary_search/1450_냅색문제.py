import sys
input = sys.stdin.readline
n, c = map(int, input().split())
data = list(map(int, input().split()))

def sub(idx, end):
    subs = [0]
    for i in range(idx, end):
        x = data[i]
        n = len(subs)
        for j in range(n):
            subs.append(subs[j] + x)
    return subs


mid = n // 2
sub_left = sub(0, mid)
sub_right = sub(mid, n)
sub_left.sort()
sub_right.sort()

def find(target, arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

ans = 0
for i in sub_left:
    target = c - i
    if c < 0: continue
    ans += find(target, sub_right)

print(ans)
