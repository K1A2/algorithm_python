import sys
input = lambda: sys.stdin.readline()

def init_tree(node, left, right):
    if left == right:
        tree[node] = data[left - 1]
        return tree[node]
    mid = (left + right) // 2
    tree[node] = init_tree(node * 2, left, mid) ^ init_tree(node * 2 + 1, mid + 1, right)
    return tree[node]

def propagate(node, left, right):
    if not lazy[node]:
        return
    tree[node] ^= lazy[node] * ((right - left + 1) % 2)
    if left != right:
        lazy[node * 2] ^= lazy[node]
        lazy[node * 2 + 1] ^= lazy[node]
    lazy[node] = 0

def update(node, start, end, left, right, value):
    propagate(node, left, right)
    if right < start or left > end:
        return
    if start <= left and right <= end:
        lazy[node] ^= value
        propagate(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid, value)
    update(node * 2 + 1, start, end, mid + 1, right, value)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

def query(node, start, end, left, right):
    propagate(node, left, right)
    if right < start or left > end:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) ^ query(node * 2 + 1, start, end, mid + 1, right)

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    init_tree(1, 1, n)

    for _ in range(int(input())):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(1, line[1] + 1, line[2] + 1, 1, n, line[3])
        else:
            print(query(1, line[1] + 1, line[2] + 1, 1, n))
