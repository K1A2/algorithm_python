import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
data_a = list(map(int, input().split()))
data_p = [0] * (n + 1)
for i in range(n):
    data_p[i + 1] = (data_p[i] + data_a[i]) % k
data = data_p
n += 1
# print(data)

m = int(input())
querys = []
for i in range(m):
    a, b = map(int, input().split())
    querys.append((i, a - 1, b))

block_size = int(n ** 0.5)
querys.sort(key=lambda x: (x[1] // block_size, x[2]))

index_list = defaultdict(deque)
block_count = n // block_size
if n % block_size != 0: block_count += 1
blocks = [0] * block_count
position = [0] * n

ans = [''] * m
left = 0
right = -1
for i, a, b in querys:
    while left > a:
        left -= 1
        if index_list[data[left]]:
            old = index_list[data[left]][-1] - index_list[data[left]][0]
            position[old] -= 1
            blocks[old // block_size] -= 1

        index_list[data[left]].appendleft(left)
        new = index_list[data[left]][-1] - index_list[data[left]][0]
        position[new] += 1
        blocks[new // block_size] += 1
    while right < b:
        right += 1
        if index_list[data[right]]:
            old = index_list[data[right]][-1] - index_list[data[right]][0]
            position[old] -= 1
            blocks[old // block_size] -= 1

        index_list[data[right]].append(right)
        new = index_list[data[right]][-1] - index_list[data[right]][0]
        position[new] += 1
        blocks[new // block_size] += 1
    while left < a:
        old = index_list[data[left]][-1] - index_list[data[left]][0]
        position[old] -= 1
        blocks[old // block_size] -= 1

        index_list[data[left]].popleft()
        if index_list[data[left]]:
            new = index_list[data[left]][-1] - index_list[data[left]][0]
            position[new] += 1
            blocks[new // block_size] += 1
        left += 1
    while right > b:
        old = index_list[data[right]][-1] - index_list[data[right]][0]
        position[old] -= 1
        blocks[old // block_size] -= 1

        index_list[data[right]].pop()
        if index_list[data[right]]:
            new = index_list[data[right]][-1] - index_list[data[right]][0]
            position[new] += 1
            blocks[new // block_size] += 1
        right -= 1

    res = 0
    find = 0
    for idx in range(block_count - 1, -1, -1):
        if blocks[idx] != 0:
            block_left = block_size * idx
            block_right = min(block_left + block_size, n)
            for b in range(block_right - 1, block_left - 1, -1):
                if position[b]:
                    res = b
                    find = 1
                    break
        if find: break
    ans[i] = f'{res}'
sys.stdout.write('\n'.join(ans))
