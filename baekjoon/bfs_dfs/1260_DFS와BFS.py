import copy

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dfs(graph, node, visited):
    q = graph[node]
    visited[node] = True
    print(node, end=' ')
    q.sort()
    while q:
        node = q.pop(0)
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, node, visited):
    queue = [node]
    while queue:
        q = queue.pop(0)
        if not visited[q]:
            visited[q] = True
            graph[q].sort()
            queue += graph[q]
            print(q, end=' ')

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
dfs(copy.deepcopy(graph), v, visited)
print()
visited = [False] * (n + 1)
bfs(copy.deepcopy(graph), v, visited)