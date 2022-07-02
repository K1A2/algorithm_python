import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
indegree = [[] for _ in range(n + 1)]
connect = [set() for _ in range(n + 1)]
recipe = [[] for _ in range(n + 1)]
for _ in range(m):
    l = list(map(int, input().rstrip().split()))
    r = set()
    for i in range(1, l[0] + 1):
        r.add(l[i])
        connect[l[i]].add(l[-1])
    recipe[l[-1]].append(r)
    indegree[l[-1]].append(l[0])
g = int(input().rstrip())
d = deque()
can = [0] * (n + 1)
for i in map(int, input().rstrip().split()):
    d.append(i)
    can[i] = 1
while d:
    now = d.popleft()
    for c in connect[now]:
        for idx, r in enumerate(recipe[c]):
            if now in r: indegree[c][idx] -= 1
            if not indegree[c][idx] and not can[c]:
                d.append(c)
                can[c] = 1
res = [i for i in range(n + 1) if can[i]]
print(len(res))
print(*res)