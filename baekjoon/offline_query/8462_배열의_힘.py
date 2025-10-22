from collections import defaultdict
import sys
input = sys.stdin.readline
n, t = map(int, input().split())
data = list(map(int, input().split()))

query = []
for i in range(t):
    a, b = map(int, input().split())
    query.append((i, a, b))
block_size = int(n ** 0.5)
query.sort(key=lambda x: (x[1] // block_size, x[2]))

ans = ['0'] * t
left = 0
right = -1
res = 0
count = defaultdict(int)
for i, a, b in query:
    a -= 1
    b -= 1
    while left > a:
        left -= 1
        res -= count[data[left]] ** 2 * data[left]
        count[data[left]] += 1
        res += count[data[left]] ** 2 * data[left]
    while right < b:
        right += 1
        res -= count[data[right]] ** 2 * data[right]
        count[data[right]] += 1
        res += count[data[right]] ** 2 * data[right]
    while left < a:
        res -= count[data[left]] ** 2 * data[left]
        count[data[left]] -= 1
        res += count[data[left]] ** 2 * data[left]
        left += 1
    while right > b:
        res -= count[data[right]] ** 2 * data[right]
        count[data[right]] -= 1
        res += count[data[right]] ** 2 * data[right]
        right -= 1
    ans[i] = f'{res}'
sys.stdout.write('\n'.join(ans))
