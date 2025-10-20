import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

# max_val, all_bits_and, all_bits_or, lazy_and, lazy_o
tree = [[0, 0, 0, (1 << 20) - 1, 0] for _ in range(n * 4)]


def init(node, left, right):
    if left == right:
        num = data[left - 1]
        tree[node] = [num, num, num, (1 << 20) - 1, 0]
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)
    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = tree[node * 2][1] & tree[node * 2 + 1][1]
    tree[node][2] = tree[node * 2][2] | tree[node * 2 + 1][2]

init(1, 1, n)


def propagation(node):
    if tree[node][3] == (1 << 20) - 1 and tree[node][4] == 0:
        return

    for child in [node * 2, node * 2 + 1]:
        tree[child][0] = (tree[child][0] & tree[node][3]) | tree[node][4]
        tree[child][1] = (tree[child][1] & tree[node][3]) | tree[node][4]
        tree[child][2] = (tree[child][2] & tree[node][3]) | tree[node][4]

        tree[child][3] &= tree[node][3]
        tree[child][4] = (tree[child][4] & tree[node][3]) | tree[node][4]

    tree[node][3] = (1 << 20) - 1
    tree[node][4] = 0


def update_and(node, start, end, left, right, value):
    if right < start or end < left:
        return

    diff = tree[node][2] & (~tree[node][1])
    mask = ~value

    if start <= left and right <= end:
        if diff & mask == 0:
            tree[node][0] &= value
            tree[node][1] &= value
            tree[node][2] &= value
            tree[node][3] &= value
            tree[node][4] &= value
            return

    propagation(node)

    mid = (left + right) // 2
    update_and(node * 2, start, end, left, mid, value)
    update_and(node * 2 + 1, start, end, mid + 1, right, value)

    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = tree[node * 2][1] & tree[node * 2 + 1][1]
    tree[node][2] = tree[node * 2][2] | tree[node * 2 + 1][2]


def update_or(node, start, end, left, right, value):
    if right < start or end < left:
        return

    diff = tree[node][2] & (~tree[node][1])

    if start <= left and right <= end:
        if diff & value == 0:
            tree[node][0] |= value
            tree[node][1] |= value
            tree[node][2] |= value
            tree[node][4] |= value
            return

    propagation(node)

    mid = (left + right) // 2
    update_or(node * 2, start, end, left, mid, value)
    update_or(node * 2 + 1, start, end, mid + 1, right, value)

    tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = tree[node * 2][1] & tree[node * 2 + 1][1]
    tree[node][2] = tree[node * 2][2] | tree[node * 2 + 1][2]


def query_max(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node][0]

    propagation(node)

    mid = (left + right) // 2
    return max(
        query_max(node * 2, start, end, left, mid),
        query_max(node * 2 + 1, start, end, mid + 1, right)
    )


for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, l, r, x = q
        update_and(1, l, r, 1, n, x)
    elif q[0] == 2:
        _, l, r, x = q
        update_or(1, l, r, 1, n, x)
    elif q[0] == 3:
        _, l, r = q
        sys.stdout.write(f'{query_max(1, l, r, 1, n)}\n')
