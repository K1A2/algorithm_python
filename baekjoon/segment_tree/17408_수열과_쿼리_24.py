import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
tree = [[0, 0] for _ in range(4 * n)]

def init(node, left, right):
    if left == right:
        tree[node][0] = data[left - 1]
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)
    temp = tree[node * 2] + tree[node * 2 + 1]
    temp.sort()
    tree[node] = [temp[-1], temp[-2]]

init(1, 1, n)


def update(node, left, right, target, value):
    if left == right:
        tree[node][0] = value
        return
    mid = (left + right) // 2
    if target <= mid:
        update(node * 2, left, mid, target, value)
    else:
        update(node * 2 + 1, mid + 1, right, target, value)
    temp = tree[node * 2] + tree[node * 2 + 1]
    temp.sort()
    tree[node] = [temp[-1], temp[-2]]

def query(node, start, end, left, right):
    if right < start or end < left:
        return [0, 0]
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    tmp = query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)
    tmp.sort()
    return [tmp[-1], tmp[-2]]

# print(tree)

for _ in range(int(input())):
    i, a, b = map(int, input().split())
    if i == 1:
        update(1, 1, n, a, b)
        # print(tree)
    elif i == 2:
        sys.stdout.write(f'{sum(query(1, a, b, 1, n))}\n')
