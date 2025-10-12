import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

index_data = []
for i in range(n):
    index_data.append((data[i], i))
index_data.sort()

tree = [0] * (4 * n)

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + \
        query(node * 2 + 1, start, end, mid + 1, right)

def update(node, left, right, index):
    if left == right:
        tree[node] = 1
        return
    mid = (left + right) // 2
    if index <= mid:
        update(node * 2, left, mid, index)
    else:
        update(node * 2 + 1, mid + 1, right, index)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

ans = 0
for d, idx in index_data:
    ans += query(1, idx + 1, n, 1, n)
    update(1, 1, n, idx + 1)
sys.stdout.write(f'{ans}')
