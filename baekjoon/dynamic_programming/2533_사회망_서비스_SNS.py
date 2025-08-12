import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)

def dfs(node):
    dp[node][1] = 1
    visited[node] = 1
    for n_node in graph[node]:
        if visited[n_node]: continue
        dfs(n_node)
        dp[node][0] += dp[n_node][1]
        dp[node][1] += min(dp[n_node])
dfs(1)
print(min(dp[1]))
