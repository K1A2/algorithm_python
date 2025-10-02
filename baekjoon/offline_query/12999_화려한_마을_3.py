import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(lambda x: int(x) + 100000, input().split()))
query = []
for i in range(m):
    a, b = map(int, input().split())
    query.append((i, a - 1, b - 1))
sqrtn = n ** 0.5
query.sort(key=lambda x: (x[1] // sqrtn, x[2]))

ans = [''] * m
left = 0
right = -1
numbers = [0] * 200002
count = [0] * 200002
max_count = 0

for i, a, b in query:
    while left < a:
        if numbers[data[left]] == max_count and count[max_count] == 1:
            max_count = numbers[data[left]] - 1
        count[numbers[data[left]]] -= 1
        numbers[data[left]] -= 1
        count[numbers[data[left]]] += 1
        left += 1
    while left > a:
        left -= 1
        count[numbers[data[left]]] -= 1
        numbers[data[left]] += 1
        count[numbers[data[left]]] += 1
        max_count = max(max_count, numbers[data[left]])
    while right < b:
        right += 1
        count[numbers[data[right]]] -= 1
        numbers[data[right]] += 1
        count[numbers[data[right]]] += 1
        max_count = max(max_count, numbers[data[right]])
    while right > b:
        if numbers[data[right]] == max_count and count[max_count] == 1:
            max_count = numbers[data[right]] - 1
        count[numbers[data[right]]] -= 1
        numbers[data[right]] -= 1
        count[numbers[data[right]]] += 1
        right -= 1
    ans[i] = str(max_count)
sys.stdout.write('\n'.join(ans))
