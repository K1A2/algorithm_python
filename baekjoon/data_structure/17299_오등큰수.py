from collections import defaultdict, deque
n = int(input())
data = list(map(int, input().split()))
count = defaultdict(int)
for d in data:
    count[d] += 1
q = deque()
q.append((data[0], 0))
ans = [0] * n
for i in range(1, n):
    while len(q) > 0 and count[q[-1][0]] < count[data[i]]:
        _, idx = q.pop()
        ans[idx] = data[i]
    q.append((data[i], i))
while len(q) > 0:
    _, idx = q.pop()
    ans[idx] = -1
print(' '.join(map(str, ans)))
