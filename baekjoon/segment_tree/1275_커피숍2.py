import sys
input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1
segment_tree = [0] * (2 * size)
size -= 1


def init():
    for i in range(n):
        segment_tree[size + i + 1] = data[i]
    for i in range(size - 1, 0, -1):
        segment_tree[i] = segment_tree[i * 2] + segment_tree[i * 2 + 1]


def update(node, value):
    node += size
    while node:
        segment_tree[node] += value
        node //= 2


def query(left, right):
    left += size
    right += size
    ans = 0
    while left <= right:
        if left % 2 == 1:
            ans += segment_tree[left]
            left += 1
        left //= 2

        if right % 2 == 0:
            ans += segment_tree[right]
            right -= 1
        right //= 2
    return ans


init()

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    print(query(x, y))
    update(a, b - segment_tree[size + a])
