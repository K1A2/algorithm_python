n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    node, to = map(int, input().split())
    graph[node].append(to)
    graph[to].append(node)

def dfs(graph, node, visited, count):
    visited[node] = True
    graph[node].sort()
    v = graph[node]
    while v:
        now = v.pop(0)
        if not visited[now]:
            count = dfs(graph, now, visited, count + 1)
    return count

visited = [False] * (n + 1)
print(dfs(graph, 1, visited, 0))
