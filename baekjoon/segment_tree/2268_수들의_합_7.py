import sys
input = lambda: sys.stdin.readline()

def update(node, value):
    node += size
    segment_tree[node] = value
    node //= 2
    while node:
        segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]
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


if __name__ == '__main__':
    n, m = map(int, input().split())
    size = 1
    while size < n:
        size <<= 1
    segment_tree = [0] * (2 * size)
    size -= 1

    for _ in range(m):
        line = list(map(int, input().split()))
        if line[0] == 0:
            if line[1] > line[2]:
                line[1], line[2] = line[2], line[1]
            print(query(line[1], line[2]))
        else:
            update(line[1], line[2])
