import sys
input = lambda: sys.stdin.readline()

def init_segment(node, left, right):
    if left == right:
        tree[node] = left
        return
    mid = (left + right) // 2
    init_segment(node * 2, left, mid)
    init_segment(node * 2 + 1, mid + 1, right)
    if value[tree[node * 2]] < value[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    elif value[tree[node * 2]] > value[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2 + 1]
    else:
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def update(node, left, right, idx, v):
    if left == right:
        value[idx] = v
        return
    if left > idx or idx > right:
        return
    mid = (left + right) // 2
    update(node * 2, left, mid, idx, v)
    update(node * 2 + 1, mid + 1, right, idx, v)

    if value[tree[node * 2]] < value[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    elif value[tree[node * 2]] > value[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2 + 1]
    else:
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(node, left, right, start, end):
    if right < start or left > end:
        return -1
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    node_1 = query(node * 2, left, mid, start, end)
    node_2 = query(node * 2 + 1, mid + 1, right, start, end)
    if node_1 == -1 and node_2 == -1:
        return -1
    if node_1 == -1:
        return node_2
    if node_2 == -1:
        return node_1
    if value[node_1] < value[node_2]:
        return node_1
    if value[node_1] > value[node_2]:
        return node_2
    return min(node_1, node_2)

if __name__ == '__main__':
    n = int(input())
    value = [0] + list(map(int, input().split()))
    tree = [0] * (4 * n)
    init_segment(1, 1, n)

    for i in range(int(input())):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(1, 1, n, line[1], line[2])
        else:
            print(query(1, 1, n, line[1], line[2]))
