import sys
input = sys.stdin.readline

while True:
    try:
        n, k = map(int, input().split())
        data = list(map(int, input().split()))
    except:
        break

    base = 1
    while base < n:
        base <<= 1
    seg = [(0, 0)] * (2 * base)

    def merge(a, b):
        return (a[0] + b[0], a[1] + b[1])

    for i in range(n):
        if data[i] == 0:
            seg[base + i] = (1, 0)
        elif data[i] > 0:
            seg[base + i] = (0, 0)
        else:
            seg[base + i] = (0, 1)

    for i in range(base - 1, 0, -1):
        seg[i] = merge(seg[i << 1], seg[i << 1 | 1])

    def update(idx, val):
        pos = base + idx
        if val == 0:
            seg[pos] = (1, 0)
        elif val > 0:
            seg[pos] = (0, 0)
        else:
            seg[pos] = (0, 1)

        pos >>= 1
        while pos:
            seg[pos] = merge(seg[pos << 1], seg[pos << 1 | 1])
            pos >>= 1

    def query(l, r):
        l += base
        r += base
        left_acc = (0, 0)
        right_acc = (0, 0)
        while l <= r:
            if (l & 1) == 1:
                left_acc = merge(left_acc, seg[l])
                l += 1
            if (r & 1) == 0:
                right_acc = merge(seg[r], right_acc)
                r -= 1
            l >>= 1
            r >>= 1
        zero_cnt, neg_cnt = merge(left_acc, right_acc)
        if zero_cnt > 0:
            return '0'
        return '-' if neg_cnt % 2 else '+'

    out = []
    for _ in range(k):
        c, a, b = input().split()
        a, b = int(a), int(b)
        if c == 'C':
            update(a - 1, b)
        else:
            out.append(query(a - 1, b - 1))
    sys.stdout.write(''.join(out) + '\n')
