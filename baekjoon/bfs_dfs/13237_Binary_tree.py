import sys
from collections import deque
input = lambda : sys.stdin.readline()
n = int(input())
graph = [[] for _ in range(n + 1)]
start = 1
for i in range(n):
    j = int(input())
    if j == -1:
        start = i + 1
        continue
    graph[j].append(i + 1)
answer = [0] * n
q = deque()
q.append((start, 0))
while q:
    node, dist = q.popleft()
    for next_node in graph[node]:
        answer[next_node - 1] = dist + 1
        q.append((next_node, dist + 1))
for i in answer:
    print(i)
