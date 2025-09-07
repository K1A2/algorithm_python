n, m = map(int, input().split())

segment_tree = [[0, 0] for _ in range(n * 4)]

def propagate(node, left, right):
    if segment_tree[node][1] == 0:
        return
    segment_tree[node][0] = (right - left + 1) - segment_tree[node][0]
    if left != right:
        segment_tree[node * 2][1] ^= 1
        segment_tree[node * 2 + 1][1] ^= 1
    segment_tree[node][1] = 0

def update(node, start, end, left, right):
    propagate(node, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        segment_tree[node][1] ^= 1
        propagate(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid)
    update(node * 2 + 1, start, end, mid + 1, right)
    segment_tree[node][0] = segment_tree[node * 2][0] + segment_tree[node * 2 + 1][0]

def query(node, start, end, left, right):
    propagate(node, left, right)
    if right < start or left > end:
        return 0
    if start <= left and right <= end:
        return segment_tree[node][0]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0: # update
        update(1, a, b, 1, n)
    else: # count
        print(query(1, a, b, 1, n))
