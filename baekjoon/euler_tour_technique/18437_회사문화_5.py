import sys
from collections import deque
input = lambda: sys.stdin.readline()

def euler(node):
    idx = 0
    stack = deque()
    stack.append((node, 0))
    while stack:
        current_node, visited = stack.pop()
        if not visited:
            idx += 1
            range_in[current_node] = idx
            stack.append((current_node, 1))
            for child in graph[current_node]:
                if range_in[child] == 0:
                    stack.append((child, 0))
        else:
            range_out[current_node] = idx

def propagate(node, left, right):
    if lazy[node] == -1:
        return
    segment_tree[node] = lazy[node] * (right - left + 1)
    if left != right:
        lazy[node * 2] = lazy[node]
        lazy[node * 2 + 1] = lazy[node]
    lazy[node] = -1

def update(node, start, end, left, right, value):
    propagate(node, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        lazy[node] = value
        propagate(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid, value)
    update(node * 2 + 1, start, end, mid + 1, right, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def query(node, start, end, left, right):
    propagate(node, left, right)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segment_tree[node]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for idx, p in enumerate(map(int, input().split()), 1):
        if idx == 1:
            continue
        graph[p].append(idx)

    range_in = [0] * (n + 1)
    range_out = [0] * (n + 1)
    euler(1)

    segment_tree = [0] * (4 * n)
    lazy = [-1] * (4 * n)

    for i in range(1, n + 1):
        update(1, i, i, 1, n, 1)

    for _ in range(int(input())):
        line = list(map(int, input().split()))
        target = line[1]
        if line[0] == 1:
            update(1, range_in[target] + 1, range_out[target], 1, n, 1)
        elif line[0] == 2:
            update(1, range_in[target] + 1, range_out[target], 1, n, 0)
        else:
            print(query(1, range_in[target] + 1, range_out[target], 1, n))
