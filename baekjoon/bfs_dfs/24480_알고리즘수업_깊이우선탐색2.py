import sys
sys.setrecursionlimit(10 ** 8)

input = lambda : sys.stdin.readline()
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
order = [0] * (n + 1)
count = 1

def dfs(now_node, count):
    for next_node in sorted(graph[now_node], reverse=True):
        if order[next_node] == 0:
            count += 1
            order[next_node] = count
            count = dfs(next_node, count)
    return count
order[r] = 1
dfs(r, 1)
for i in range(1, n + 1):
    print(order[i])
