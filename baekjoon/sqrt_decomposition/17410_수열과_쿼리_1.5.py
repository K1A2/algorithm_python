import sys
from bisect import bisect_right, bisect_left
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
    if value == data[target]:
        return
    group_idx = target // sqrt_v
    block = group_data[group_idx]

    block_target_pos = bisect_left(block, data[target])
    block.pop(block_target_pos)

    block_new_pos = bisect_right(block, value)
    block.insert(block_new_pos, value)

    data[target] = value


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
        _, i, k = q
        update(i - 1, k)
    else:
        _, i, j, k = q
        sys.stdout.write(f'{query(i - 1, j - 1, k)}\n')
