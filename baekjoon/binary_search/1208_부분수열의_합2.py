import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
mid = n // 2

def sub(idx, end):
    sublist = []
    dq = deque()
    dq.append((idx, 0, 0))

    while dq:
        idx, curr_sum, used = dq.popleft()
        if idx == end:
            if used:
                sublist.append(curr_sum)
        else:
            dq.append((idx + 1, curr_sum, used))
            dq.append((idx + 1, curr_sum + data[idx], 1))
    return sublist

sub_left = sub(0, mid)
sub_right = sub(mid, n)
sub_right.sort()

def find(target, arr, mode=0):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if mode == 0:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
    return left

ans = 0
for i in sub_left:
    target = m - i
    ans += find(target, sub_right, 1) - find(target, sub_right)

target = m
sub_left.sort()
ans += find(target, sub_left, 1) - find(target, sub_left)
ans += find(target, sub_right, 1) - find(target, sub_right)

print(ans)
