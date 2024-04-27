import sys
input = lambda: sys.stdin.readline()

def concatenate(a, b):
    if a[0] == b[0]:
        return [a[0], max(a[1], b[1]), a[2] + b[2], a[3] + b[3]]
    if a[0] > b[0]:
        a, b = b, a
    return [b[0], max(a[0], b[1]), b[2], a[3] + b[3]]

def init(node, left, right):
    if left == right:
        segment_tree[node] = [data[left - 1], -float('inf'), 1, data[left - 1]]
        return segment_tree[node]
    mid = (left + right) // 2
    segment_tree[node] = concatenate(init(node * 2, left, mid), init(node * 2 + 1, mid + 1, right))
    return segment_tree[node]

def propagation(node, left, right):
    if left == right:
        return
    for child_node in (node * 2, node * 2 + 1):
        if segment_tree[child_node][0] > segment_tree[node][0]:
            segment_tree[child_node][3] -= segment_tree[child_node][2] * (segment_tree[child_node][0] - segment_tree[node][0])
            segment_tree[child_node][0] = segment_tree[node][0]

def update(node, start, end, left, right, value):
    propagation(node, left, right)
    if left > end or right < start or segment_tree[node][0] <= value:
        return
    if start <= left and right <= end and segment_tree[node][1] < value:
        segment_tree[node][3] -= segment_tree[node][2] * (segment_tree[node][0] - value)
        segment_tree[node][0] = value
        propagation(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid, value)
    update(node * 2 + 1, start, end, mid + 1, right, value)
    segment_tree[node] = concatenate(segment_tree[node * 2], segment_tree[node * 2 + 1])

def get_max(node, start, end, left, right):
    propagation(node, left, right)
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        return segment_tree[node][0]
    mid = (left + right) // 2
    return max(get_max(node * 2, start, end, left, mid), get_max(node * 2 + 1, start, end, mid + 1, right))

def get_sum(node, start, end, left, right):
    propagation(node, left, right)
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        return segment_tree[node][3]
    mid = (left + right) // 2
    return get_sum(node * 2, start, end, left, mid) + get_sum(node * 2 + 1, start, end, mid + 1, right)

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    segment_tree = [[] for _ in range(4 * n)]
    init(1, 1, n)

    for _ in range(int(input())):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(1, line[1], line[2], 1, n, line[3])
        elif line[0] == 2:
            print(get_max(1, line[1], line[2], 1, n))
        elif line[0] == 3:
            print(get_sum(1, line[1], line[2], 1, n))
