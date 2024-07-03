import sys
sys.setrecursionlimit(10 ** 8)

input = lambda : sys.stdin.readline()
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
depth = [-1] * (n + 1)
count = 1

def dfs(now_node, count):
    for next_node in sorted(graph[now_node], reverse=True):
        if depth[next_node] == -1:
            depth[next_node] = count
            dfs(next_node, count + 1)
depth[r] = 0
dfs(r, 1)
for i in range(1, n + 1):
    print(depth[i])
