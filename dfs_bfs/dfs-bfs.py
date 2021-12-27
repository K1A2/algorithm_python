def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True

    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
print('DFS:', end=' ')
dfs(graph, 1, visited)
print('\nBFS:', end=' ')
visited = [False] * 9
bfs(graph, 1, visited)