import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def init_segment(node, left, right):
    if left == right:
        tree[node] = left
        return
    mid = (left + right) // 2
    init_segment(node * 2, left, mid)
    init_segment(node * 2 + 1, mid + 1, right)
    tree[node] = tree[node * 2] if data[tree[node * 2]] <= data[tree[node * 2 + 1]] else tree[node * 2 + 1]

def query(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    q1 = query(node * 2, start, end, left, mid)
    q2 = query(node * 2 + 1, start, end, mid + 1, right)
    if q1 == -1:
        return q2
    if q2 == -1:
        return q1
    return q1 if data[q1] < data[q2] else q2

def calculate_area(left, right):
    idx = query(1, left, right, 0, n - 1)
    area = (right - left + 1) * data[idx]
    if left < idx:
        new_area = calculate_area(left, idx - 1)
        area = max(area, new_area)
    if idx < right:
        new_area = calculate_area(idx + 1, right)
        area = max(area, new_area)
    return area

if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]

    tree = [-1] * (4 * n)
    init_segment(1, 0, n - 1)

    print(calculate_area(0, n - 1))
