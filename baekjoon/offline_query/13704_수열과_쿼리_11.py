import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
data = [0] + list(map(int, input().split()))
n += 1
for i in range(1, n):
    data[i] ^= data[i - 1]

m = int(input())
querys = []
for i in range(m):
    a, b = map(int, input().split())
    querys.append((i, a - 1, b))

block_size = int(n ** 0.5)
querys.sort(key=lambda x: (x[1] // block_size, x[2]))

count = defaultdict(int)

ans = [''] * m
left = 0
right = -1
res = 0
for i, a, b in querys:
    while left > a:
        left -= 1
        res += count[data[left] ^ k]
        count[data[left]] += 1
    while right < b:
        right += 1
        res += count[data[right] ^ k]
        count[data[right]] += 1
    while left < a:
        count[data[left]] -= 1
        res -= count[data[left] ^ k]
        left += 1
    while right > b:
        count[data[right]] -= 1
        res -= count[data[right] ^ k]
        right -= 1
    ans[i] = f'{res}'
sys.stdout.write('\n'.join(ans))
