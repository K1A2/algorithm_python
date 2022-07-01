import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]
parents = [[] for _ in range(n + 1)]
in_count = [0] * (n + 1)
for _ in range(int(input().rstrip())):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((b, t))
    in_count[b] += 1
s, f = map(int, input().rstrip().split())
d = deque()
d.append((s, 0))
while d:
    now, t = d.popleft()
    for i in graph[now]:
        if result[now] + i[1] >= result[i[0]] or t + i[1] >= result[i[0]]:
            if result[now] + i[1] > t + i[1]:
                if result[now] + i[1] > result[i[0]]:
                    parents[i[0]] = [now]
                else:
                    parents[i[0]].append(now)
                result[i[0]] = result[now] + i[1]
            else:
                if t + i[1] > result[i[0]]:
                    parents[i[0]] = [now]
                else:
                    parents[i[0]].append(now)
                result[i[0]] = t + i[1]
        in_count[i[0]] -= 1
        if not in_count[i[0]]:
            d.append((i[0], t + i[1]))
visited = [0] * (n + 1)
d.append(f)
visited[f] = 1
roads_count = 0
while d:
    for i in parents[d.popleft()]:
        roads_count += 1
        if not visited[i]:
            d.append(i)
            visited[i] = 1
print(f'{result[f]}\n{roads_count}')