import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
data = map(int, input().rstrip().split())
delete = int(input())
trees = [[] for _ in range(n)]
root = -1
for idx, n in enumerate(data):
    if idx != delete:
        if n != -1:
            if n != delete:
                trees[n].append(idx)
        else:
            root = idx
if root == -1:
    print(0)
    exit()
q = deque()
asw = 0
if trees[root]:
    for i in trees[root]:
        q.append(i)
else:
    print(asw + 1)
    exit()
while q:
    now = q.popleft()
    if not trees[now]:
        asw += 1
    else:
        for i in trees[now]:
            q.appendleft(i)
print(asw)