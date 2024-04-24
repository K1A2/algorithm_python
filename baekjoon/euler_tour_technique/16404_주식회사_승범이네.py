import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def propagation(node, start, end):
    if lazy[node] == 0:
        return
    segment_tree[node] += (end - start + 1) * lazy[node]
    if start != end:
        for i in range(node * 2, node * 2 + 2):
            lazy[i] += lazy[node]
    lazy[node] = 0

def update(node, start, end, left, right, value):
    propagation(node, start, end)
    if end < left or right < start:
        return
    if left <= start and end <= right:
        lazy[node] = value
        propagation(node, start, end)
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, value)
    update(node * 2 + 1, mid + 1, end, left, right, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def sum(node, start, end, left, right):
    propagation(node, start, end)
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    mid = (start + end) // 2
    return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right)

def dfs(node, order_num):
    range_in[node] = order_num
    for next_node in graph[node]:
        order_num = dfs(next_node, order_num + 1)
    range_out[node] = order_num
    return order_num

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parents = list(map(int, input().split()))
for i, a in enumerate(parents, 1):
    if a == -1:
        continue
    graph[a].append(i)

range_in = [0] * (n + 1)
range_out = [0] * (n + 1)
dfs(1, 1)

segment_tree = [0] * (4 * (n + 1))
lazy = [0] * (4 * (n + 1))

results = []
for _ in range(m):
    line = list(map(int, input().split()))
    target = line[1]
    if line[0] == 1:
        update(1, 1, n, range_in[target], range_out[target], line[2])
    else:
        a = line[1]
        print(sum(1, 1, n, range_in[target], range_in[target]))
