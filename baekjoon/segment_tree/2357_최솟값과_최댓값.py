import sys
input = lambda: sys.stdin.readline()

def update(node, value):
    node += size
    segment_tree[node][0] = value
    segment_tree[node][1] = value
    node //= 2
    while node:
        segment_tree[node][1] = min(segment_tree[node * 2][1], segment_tree[node * 2 + 1][1])
        segment_tree[node][0] = max(segment_tree[node * 2][0], segment_tree[node * 2 + 1][0])
        node //= 2

def query(left, right):
    left += size
    right += size
    ans_min = int(1e10)
    ans_max = 0
    while left <= right:
        if left % 2 == 1:
            ans_min = min(ans_min, segment_tree[left][1])
            ans_max = max(ans_max, segment_tree[left][0])
            left += 1
        left //= 2

        if right % 2 == 0:
            ans_min = min(ans_min, segment_tree[right][1])
            ans_max = max(ans_max, segment_tree[right][0])
            right -= 1
        right //= 2
    return str(ans_min), str(ans_max)


if __name__ == '__main__':
    n, m = map(int, input().split())
    size = 1
    while size < n:
        size <<= 1
    segment_tree = [[0, int(1e10)] for _ in range(2 * size)]
    size -= 1

    for idx in range(1, n + 1):
        update(idx, int(input()))

    for _ in range(m):
        a, b = map(int, input().split())
        print(' '.join(query(a, b)))
