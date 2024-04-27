import sys
input = lambda: sys.stdin.readline()

def update(node, value):
    node += size
    segment_tree[node] = value
    node //= 2
    while node:
        segment_tree[node] = min(segment_tree[node * 2], segment_tree[node * 2 + 1])
        node //= 2

def query(left, right):
    left += size
    right += size
    ans_min = int(1e10)
    while left <= right:
        if left % 2 == 1:
            ans_min = min(ans_min, segment_tree[left])
            left += 1
        left //= 2

        if right % 2 == 0:
            ans_min = min(ans_min, segment_tree[right])
            right -= 1
        right //= 2
    return str(ans_min)


if __name__ == '__main__':
    n, m = map(int, input().split())
    size = 1
    while size < n:
        size <<= 1
    segment_tree = [int(1e10)] * (2 * size)
    size -= 1

    for idx in range(1, n + 1):
        update(idx, int(input()))

    for _ in range(m):
        a, b = map(int, input().split())
        print(query(a, b))
