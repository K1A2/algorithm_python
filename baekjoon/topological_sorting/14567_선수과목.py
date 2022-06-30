import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
in_count = [0] * (n + 1)
for _ in range(m):
    a ,b = map(int, input().rstrip().split())
    graph[a].append(b)
    in_count[b] += 1

def topological_sort():
    d = deque()
    result = [0] * n
    for i in range(1, n + 1):
        if not in_count[i]:
            d.append((i, 1))
    while d:
        now, c = d.popleft()
        result[now - 1] = c
        for i in graph[now]:
            in_count[i] -= 1
            if not in_count[i]:
                d.append((i, c + 1))
    return result
print(*topological_sort())