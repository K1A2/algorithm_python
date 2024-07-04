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

def dfs(now_node, count, order, ans):
    for next_node in sorted(graph[now_node]):
        if depth[next_node] == -1:
            order += 1
            depth[next_node] = count
            ans, order = dfs(next_node, count + 1, order, ans + order * count)
    return ans, order
depth[r] = 0
print(dfs(r, 1, 1, 0)[0])
