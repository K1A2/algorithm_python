import sys
from bisect import bisect_right
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

sqrt_v = int(n ** 0.5)
group_count = n // sqrt_v
if n % sqrt_v != 0:
    group_count += 1
group_data = [[] for _ in range(group_count)]

for i in range(0, n, sqrt_v):
    end = i + sqrt_v
    if end > n:
        end = n
    group_data[i // sqrt_v] = data[i:end]
    group_data[i // sqrt_v].sort()


def update(target, value):
    data[target] = value
    group_idx = target // sqrt_v
    s = group_idx * sqrt_v
    e = s + sqrt_v
    if e > n:
        e = n
    group_data[target // sqrt_v] = data[s:e]
    group_data[target // sqrt_v].sort()


def query(left, right, value):
    ans = 0
    while left % sqrt_v and left <= right:
        if data[left] > value:
            ans += 1
        left += 1
    while (right + 1) % sqrt_v and left <= right:
        if data[right] > value:
            ans += 1
        right -= 1
    while left <= right:
        ans += len(group_data[left // sqrt_v]) - bisect_right(group_data[left // sqrt_v], value)
        left += sqrt_v
    return ans


for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, i, j, k = q
        sys.stdout.write(f'{query(i - 1, j - 1, k)}\n')
    else:
        _, i, k = q
        update(i - 1, k)
