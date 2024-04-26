import sys
input = lambda: sys.stdin.readline()

def propagation(node, left, right):
    if not lazy[node]:
        return
    segment_tree[node] += (right - left + 1) * lazy[node]
    if left != right:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0

def update(node, start, end, left, right, value):
    propagation(node, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        lazy[node] += value
        propagation(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid, value)
    update(node * 2 + 1, start, end, mid + 1, right, value)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def query(node, start, end, left, right):
    propagation(node, left, right)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segment_tree[node]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)

if __name__ == '__main__':
    n, m, k = map(int, input().split())

    segment_tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    for i in range(1, n + 1):
        value = int(input())
        update(1, i, i, 1, n, value)

    for _ in range(m + k):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(1, line[1], line[2], 1, n, line[3])
        else:
            print(query(1, line[1], line[2], 1, n))
