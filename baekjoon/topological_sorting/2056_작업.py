import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
in_count = [0] * (n + 1)
time = [0] * (n + 1)
result = [0] * n
for i in range(1, n + 1):
    l = list(map(int, input().rstrip().split()))
    time[i] = l[0]
    result[i - 1] = l[0]
    for j in range(2, 2 + l[1]):
        graph[l[j]].append(i)
        in_count[i] += 1

def topological_sort():
    d = deque()
    for i in range(1, n + 1):
        if not in_count[i]:
            d.append(i)
    while d:
        now = d.popleft()
        for i in graph[now]:
            in_count[i] -= 1
            result[i - 1] = max(result[now - 1] + time[i], result[i - 1])
            if not in_count[i]:
                d.append(i)
topological_sort()
print(max(result))