import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
m = int(input())
query = []
for i in range(m):
    a, b = map(int, input().split())
    query.append((i, a - 1, b - 1))
sqrtn = n ** 0.5
query.sort(key=lambda x: (x[1] // sqrtn, x[2]))

ans = [''] * m
count = 0
left = 0
right = -1
numbers = defaultdict(int)

for i, a, b in query:
    while left < a:
        numbers[data[left]] -= 1
        if numbers[data[left]] == 0:
            count -= 1
        left += 1
    while left > a:
        left -= 1
        if numbers[data[left]] == 0:
            count += 1
        numbers[data[left]] += 1
    while right < b:
        right += 1
        if numbers[data[right]] == 0:
            count += 1
        numbers[data[right]] += 1
    while right > b:
        numbers[data[right]] -= 1
        if numbers[data[right]] == 0:
            count -= 1
        right -= 1
    ans[i] = str(count)
sys.stdout.write('\n'.join(ans))
