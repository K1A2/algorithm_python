import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

tree = [[] for _ in range(4 * n)]


def merge(node1, node2):
    idx1 = 0
    idx2 = 0
    res = []
    while idx1 < len(node1) and idx2 < len(node2):
        if node1[idx1] <= node2[idx2]:
            res.append(node1[idx1])
            idx1 += 1
        else:
            res.append(node2[idx2])
            idx2 += 1
    while idx1 < len(node1):
        res.append(node1[idx1])
        idx1 += 1
    while idx2 < len(node2):
        res.append(node2[idx2])
        idx2 += 1
    return res


def init(node, left, right):
    if left == right:
        tree[node].append(data[left - 1])
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)
    tree[node] = merge(tree[node * 2], tree[node * 2 + 1])


def query(node, start, end, left, right, value):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return len(tree[node]) - bisect_right(tree[node], value)
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid, value) + \
        query(node * 2 + 1, start, end, mid + 1, right, value)


init(1, 1, n)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    sys.stdout.write(f'{query(1, a, b, 1, n, c)}\n')
