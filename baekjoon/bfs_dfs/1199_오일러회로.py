import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

start = -1
count = [0] * n
for idx, g in enumerate(graph):
    c = 0
    for i in g:
        c += i
    count[idx] = c
    if c and c % 2:
        print(-1)
        exit()
    if start == -1 and c > 0:
        start = idx

ans = []
proc = deque()
visited = set()

proc.append(0)
while proc:
    now = proc[-1]
    if count[now]:
        for i in range(n):
            if graph[now][i]:
                graph[now][i] -= 1
                graph[i][now] -= 1
                count[now] -= 1
                count[i] -= 1
                proc.append(i)
                break
    else:
        ans.append(proc.pop() + 1)
print(*ans)
