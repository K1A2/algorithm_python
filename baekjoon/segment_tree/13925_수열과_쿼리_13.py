import sys
input = lambda: sys.stdin.readline()

MOD = 1000000007

def propagation(node, left, right):
    if lazy[node][0] == 1 and lazy[node][1] == 0:
        return
    segment_tree[node] = (lazy[node][0] * segment_tree[node] + (right - left + 1) * lazy[node][1]) % MOD
    if left != right:
        lazy[node * 2][0] = (lazy[node * 2][0] * lazy[node][0]) % MOD
        lazy[node * 2][1] = (lazy[node][0] * lazy[node * 2][1] + lazy[node][1]) % MOD
        lazy[node * 2 + 1][0] = (lazy[node * 2 + 1][0] * lazy[node][0]) % MOD
        lazy[node * 2 + 1][1] = (lazy[node][0] * lazy[node * 2 + 1][1] + lazy[node][1]) % MOD
    lazy[node] = [1, 0]

def update(node, start, end, left, right, x, y):
    propagation(node, left, right)
    if end < left or right < start:
        return
    if start <= left and right <= end:
        lazy[node] = [x, y]
        propagation(node, left, right)
        return
    mid = (left + right) // 2
    update(node * 2, start, end, left, mid, x, y)
    update(node * 2 + 1, start, end, mid + 1, right, x, y)
    segment_tree[node] = (segment_tree[node * 2] + segment_tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    propagation(node, left, right)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return segment_tree[node]
    mid = (left + right) // 2
    return (query(node * 2, start, end, left, mid) + query(node * 2 + 1, start, end, mid + 1, right)) % MOD

if __name__ == '__main__':
    n = int(input())

    segment_tree = [0] * (4 * n)
    lazy = [[1, 0] for _ in range(4 * n)]

    data = list(map(int, input().split()))

    for idx, value in enumerate(data, 1):
        update(1, idx, idx, 1, n, 0, value)

    for _ in range(int(input())):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(1, line[1], line[2], 1, n, 1, line[3])
        elif line[0] == 2:
            update(1, line[1], line[2], 1, n, line[3], 0)
        elif line[0] == 3:
            update(1, line[1], line[2], 1, n, 0, line[3])
        else:
            print(query(1, line[1], line[2], 1, n))
