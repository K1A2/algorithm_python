import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().rstrip().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
def dfs(s, distance):
    d = deque()
    distance[s] = 0
    d.append((s, 0))
    while d:
        now, cost = d.popleft()
        if tree[now]:
            for i in tree[now]:
                if distance[i[0]] == -1:
                    d.appendleft((i[0], cost + i[1]))
                    distance[i[0]] = cost + i[1]
distance = [-1] * (n + 1)
dfs(1, distance)
m = distance.index(max(distance))
distance = [-1] * (n + 1)
dfs(m, distance)
print(max(distance))