import sys
input = lambda: sys.stdin.readline()

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


if __name__ == '__main__':
    n = int(input())
    size = 1
    while size < n:
        size <<= 1
    segment_tree = [0] * (2 * size)
    size -= 1

    for idx, v in enumerate(map(int, input().split()), 1):
        update(idx, v % 2)
    for _ in range(int(input())):
        line = list(map(int, input().split()))
        if line[0] == 1:
            update(line[1], line[2] % 2 - segment_tree[size + line[1]])
        elif line[0] == 2:
            print((line[2] - line[1] + 1) - query(line[1], line[2]))
        else:
            print(query(line[1], line[2]))
