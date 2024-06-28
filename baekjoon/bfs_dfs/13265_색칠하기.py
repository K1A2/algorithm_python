import sys
from collections import deque

def check(start, visited, graph):
    q = deque()
    q.append((start, 1))
    visited[start] = 1
    while q:
        now, color = q.pop()
        new_color = 2 if color == 1 else 1
        for next_node in graph[now]:
            if visited[next_node] != 0 and visited[next_node] == color:
                return 0
            if visited[next_node] == 0:
                visited[next_node] = new_color
                q.append((next_node, new_color))
    return 1


input = lambda : sys.stdin.readline()
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (n + 1)
    is_possible = 1
    for i in range(1, n + 1):
        if visited[i] == 0:
            result = check(i, visited, graph)
            if result == 0:
                is_possible = 0
                print('impossible')
                break
    if is_possible:
        print('possible')
