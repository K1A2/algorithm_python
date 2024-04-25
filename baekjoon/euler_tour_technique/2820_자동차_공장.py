import sys
from collections import deque
input = lambda: sys.stdin.readline()

def dfs(start):
    stack = deque([(start, -1, 'enter')])
    order_num = 0
    while stack:
        node, parent, state = stack.pop()
        if state == 'enter':
            order_num += 1
            range_in[node] = order_num
            stack.append((node, parent, 'leave'))
            for next_node in reversed(graph[node]):
                if next_node != parent:
                    stack.append((next_node, node, 'enter'))
        elif state == 'leave':
            range_out[node] = order_num
    return order_num

def propagation(node, start, end):
    if not lazy[node]:
        return
    segment_tree[node] += (end - start + 1) * lazy[node]
    if start != end:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0

def update(node, left, right, start, end, value):
    propagation(node, start, end)
    if end < left or start > right:
        return
    if left <= start and end <= right:
        lazy[node] += value
        propagation(node, start, end)
        return
    mid = (start + end) // 2
    update(node * 2, left, right, start, mid, value)
    update(node * 2 + 1, left, right, mid + 1, end, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def query(node, left, right, start, end):
    propagation(node, start, end)
    if end < left or start > right:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    mid = (start + end) // 2
    return query(node * 2, left, right, start, mid) + query(node * 2 + 1, left, right, mid + 1, end)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    income = [0] * (n + 1)
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        income[i] = data[0]
        if i != 1:
            graph[data[1]].append(i)

    range_in = [0] * (n + 1)
    range_out = [0] * (n + 1)
    dfs(1)

    segment_tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    for _ in range(m):
        line = input().split()
        target = int(line[1])
        if line[0] == 'p':
            update(1, range_in[target] + 1, range_out[target], 1, n, int(line[2]))
        else:
            print(query(1, range_in[target], range_in[target], 1, n) + income[target])
