from collections import deque, defaultdict
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    index = 1
    parent = [0] * (n + 1)
    finished = [0] * (n + 1)
    q = deque()
    new_connect = defaultdict(int)
    idx_count = 1

    def dfs(node):
        global index, idx_count
        index += 1
        parent[node] = low = index
        q.append(node)

        for g in graph[node]:
            if parent[g] == 0:
                low = min(low, dfs(g))
            else:
                if finished[g] == 0:
                    low = min(low, parent[g])

        if low == parent[node]:
            while q:
                now = q.pop()
                new_connect[now] = idx_count
                finished[now] = 1
                if now == node:
                    break
            idx_count += 1
        return low


    for i in range(1, n + 1):
        if parent[i] == 0:
            dfs(i)

    new_graph = [set() for _ in range(idx_count)]
    in_degree = [0] * idx_count
    for i in range(1, n + 1):
        for c in graph[i]:
            if new_connect[i] == new_connect[c]: continue
            new_graph[new_connect[i]].add(new_connect[c])
            in_degree[new_connect[c]] += 1

    res = 0
    for i in range(1, idx_count):
        if in_degree[i] == 0:
            q.append(i)
            res += 1

    sys.stdout.write(f'{res}\n')
