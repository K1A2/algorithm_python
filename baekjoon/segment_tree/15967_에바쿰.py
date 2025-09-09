import sys
input = sys.stdin.readline

n, q1, q2 = map(int, input().split())
data = list(map(int, input().split()))

tree = [[0, 0, 0] for _ in range(4 * n)]

def init(node, left, right):
    if left == right:
        tree[node] = [data[left - 1], 0, 0]
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)
    tree[node] = [tree[node * 2][0] + tree[node * 2 + 1][0], 0, 0]

def propagate(node, left, right):
    if tree[node][2] == 0:
        return
    tree[node][0] += (right - left + 1) * tree[node][1]
    if left != right:
        tree[node * 2][1] += tree[node][1]
        tree[node * 2 + 1][1] += tree[node][1]
        tree[node * 2][2] = 1
        tree[node * 2 + 1][2] = 1
    tree[node][1] = 0
    tree[node][2] = 0

def query(node, start, end, left, right):
    propagate(node, left, right)
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node][0]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)

def range_sum(node, start, end, left, right, value):
    propagate(node, left, right)
    if right < start or end < left:
        return
    if start <= left and right <= end:
        tree[node][1] += value
        tree[node][2] = 1
        propagate(node, left, right)
        return
    mid = (left + right) // 2
    range_sum(node * 2, start, end, left, mid, value)
    range_sum(node * 2 + 1, start, end, mid + 1, right, value)
    tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]

init(1, 1, n)

for _ in range(q1 + q2):
    c = list(map(int, input().split()))
    if c[0] == 1:
        _, a, b = c
        sys.stdout.write(f'{query(1, a, b, 1, n)}\n')
    else:
        _, a, b, value = c
        range_sum(1, a, b, 1, n, value)
