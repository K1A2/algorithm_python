import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
MOD = 1000000007

size = 1
while size < n:
    size <<= 1
segment_tree = [1] * (2 * size)
size -= 1

values = [int(input()) for _ in range(n)]

def init_tree():
    for i in range(n):
        segment_tree[size + i + 1] = values[i]
    for i in range(size - 1, 0, -1):
        segment_tree[i] = segment_tree[i * 2] * segment_tree[i * 2 + 1] % MOD

init_tree()

def update(node, value):
    node += size
    segment_tree[node] = value
    node //= 2
    while node:
        segment_tree[node] = segment_tree[node * 2] * segment_tree[node * 2 + 1] % MOD
        node //= 2

def query(left, right):
    left += size
    right += size
    ans = 1
    while left <= right:
        if left % 2 == 1:
            ans = ans * segment_tree[left] % MOD
            left += 1
        left //= 2

        if right % 2 == 0:
            ans = ans * segment_tree[right] % MOD
            right -= 1
        right //= 2
    return ans

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(query(b, c))
