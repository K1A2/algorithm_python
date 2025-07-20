import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
weight = list(map(int, input().split()))
position = list(map(int, input().split()))
tau = defaultdict(list)
for i in range(n):
    tau[position[i]].append(weight[i] * (5000 - position[i]))
position = list(set(position))
n = len(position)
position.sort()

def sub(idx, end):
    subs = []
    for i in range(idx, end):
        t_list = []
        for t in tau[position[i]]:
            for j in range(len(subs)):
                t_list.append(subs[j] + t)
            t_list.append(t)
        subs.extend(t_list)
    return subs


mid = n // 2
sub_left = sub(0, mid)
sub_right = sub(mid, n)
sub_left.sort()
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
    target = -i
    ans += find(target, sub_right, 1) - find(target, sub_right)

target = 0
sub_left.sort()
ans += find(target, sub_left, 1) - find(target, sub_left)
ans += find(target, sub_right, 1) - find(target, sub_right)
print(ans)
