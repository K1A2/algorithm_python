import sys
from collections import deque
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    graph = []
    checked = [0] * n
    asw = n
    for idx, i in enumerate(map(int, sys.stdin.readline().rstrip().split())):
        i -= 1
        if idx == i:
            graph.append(0)
            checked[i] = 1
            asw -= 1
        else:
            graph.append(i)
    for i in range(n):
        if not checked[i]:
            cycle = []
            q = deque()
            q.append((i, 1))
            while q:
                now, count = q.pop()
                checked[now] = 1
                cycle.append(now)
                if not checked[graph[now]]:
                    q.append((graph[now], count + 1))
                else:
                    for g in range(count):
                        if cycle[g] == graph[now]:
                            asw -= count - g
    print(asw)