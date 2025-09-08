import sys
input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))

tree = [[0, 0, 0, -1] for _ in range(n * 4)]

def init(node, left, right):
    if left == right:
        tree[node] = [data[left - 1], data[left - 1], 0, -1]
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)

    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = min(tree[node * 2][1], tree[node * 2 + 1][1])

def propagate(node, left, right):
    if tree[node][3] >= 0 and tree[node][2] != 0:
        tree[node][3] += tree[node][2]
        tree[node][2] = 0
    if tree[node][3] >= 0:
        tree[node][0] = tree[node][3]
        tree[node][1] = tree[node][3]
        if left != right:
            tree[node * 2][3] = tree[node][3]
            tree[node * 2 + 1][3] = tree[node][3]
            tree[node * 2][2] = 0
            tree[node * 2 + 1][2] = 0
        tree[node][3] = -1
    if tree[node][2] == 0:
        return
    tree[node][0] += tree[node][2]
    tree[node][1] += tree[node][2]
    if left != right:
        tree[node * 2][2] += tree[node][2]
        tree[node * 2 + 1][2] += tree[node][2]
    tree[node][2] = 0

def add(node, start, end, left, right, value):
    propagate(node, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        tree[node][2] += value
        propagate(node, left, right)
        return
    mid = (left + right) // 2
    add(node * 2, start, end, left, mid, value)
    add(node * 2 + 1, start, end, mid + 1, right, value)

    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = min(tree[node * 2][1], tree[node * 2 + 1][1])

def div(node, start, end, left, right, value):
    propagate(node, left, right)
    if end < left or right < start or value == 1:
        return
    if start <= left and right <= end:
        if tree[node][0] < value: # 전부 0
            tree[node][3] = 0
            propagate(node, left, right)
            return
        if tree[node][0] // value == tree[node][1] // value: # 몫이 전부 같음
            tree[node][3] = tree[node][0] // value
            propagate(node, left, right)
            return
        if tree[node][0] == tree[node][1] + 1:
            tree[node][2] += tree[node][1] // value - tree[node][1]
            propagate(node, left, right)
            return
    mid = (left + right) // 2
    div(node * 2, start, end, left, mid, value)
    div(node * 2 + 1, start, end, mid + 1, right, value)
    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = min(tree[node * 2][1], tree[node * 2 + 1][1])

def max_range(node, start, end, left, right):
    propagate(node, left, right)
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        return tree[node][0]
    mid = (left + right) // 2
    return max(max_range(node * 2, start, end, left, mid), max_range(node * 2 + 1, start, end, mid + 1, right))

init(1, 1, n)

for _ in range(q):
    t, l, r, x = map(int, input().split())
    if t == 0:
        add(1, l + 1, r + 1, 1, n, x)
    elif t == 1:
        div(1, l + 1, r + 1, 1, n, x)
    else:
        sys.stdout.write(f"{max_range(1, l + 1, r + 1, 1, n)}\n")
