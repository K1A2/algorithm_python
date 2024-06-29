import sys
from collections import deque
input = lambda : sys.stdin.readline()

def check(graph):
    q = deque()
    q.append(0)
    visited = [0] * len(graph)
    visited[0] = 1
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)
    if sum(visited) == len(graph):
        return 'Connected.'
    return 'Not connected.'

for _ in range(int(input())):
    data = list(map(int, input().split()))
    n = data[0]
    graph = [[] for _ in range(n)]
    for i in range(data[1]):
        a, b = data[2 + i * 2], data[2 + i * 2 + 1]
        graph[a].append(b)
        graph[b].append(a)
    print(check(graph))
