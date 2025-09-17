import sys
input = sys.stdin.readline
def init(tree, init_pos, node, left, right):
    if left == right:
        tree[node] = init_pos[left - 1]
        return
    mid = (left + right) // 2
    init(tree, init_pos, node * 2, left, mid)
    init(tree, init_pos, node * 2 + 1, mid + 1, right)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return query(tree, node * 2, start, end, left, mid) + \
        query(tree, node * 2 + 1, start, end, mid + 1, right)

def update(tree, node, left, right, idx, value):
    if left == right:
        tree[node] += value
        return tree[node]
    mid = (left + right) // 2
    if idx < mid:
        update(tree, node * 2, left, mid, idx, value)
    else:
        update(tree, node * 2 + 1, mid + 1, right, idx, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    watch = list(map(int, input().split()))
    pos = [i + m for i in range(n)]
    init_pos = [0] * m + [1] * n
    tree = [0] * (4 * (n + m))
    init(tree, init_pos, 1, 1, n + m)
    # print(tree, pos, init_pos)

    for i in range(m):
        w = watch[i]
        sys.stdout.write(f'{query(tree, 1, 1, pos[w - 1], 1, n + m)} ')
        update(tree, 1, 1, n + m, pos[w - 1], -1)
        pos[w - 1] = m - i - 1
        update(tree, 1, 1, n + m, pos[w - 1], 1)
    sys.stdout.write('\n')
