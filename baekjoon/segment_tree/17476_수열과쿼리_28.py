# 문제 제출은 C++로 변환해서 정답

import sys
import math
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def merge_node(L, R):
    return [L[0] + R[0], min(L[1], R[1]), max(L[2], R[2]), 0, False, 0]

def apply_set(seg, node, seg_len, v):
    nd = seg[node]
    nd[0] = v * seg_len
    nd[1] = v
    nd[2] = v
    nd[4] = True
    nd[5] = v
    nd[3] = 0

def apply_add(seg, node, seg_len, v):
    nd = seg[node]
    nd[0] += v * seg_len
    nd[1] += v
    nd[2] += v
    if nd[4]:
        nd[5] += v
    else:
        nd[3] += v

def build(seg, arr, node, l, r):
    if l == r:
        v = arr[l - 1]
        seg[node] = [v, v, v, 0, False, 0]
        return seg[node]
    m = (l + r) // 2
    L = build(seg, arr, node * 2, l, m)
    R = build(seg, arr, node * 2 + 1, m + 1, r)
    seg[node] = merge_node(L, R)
    return seg[node]

def push(seg, node, l, r):
    nd = seg[node]
    if l == r:
        nd[3] = 0
        nd[4] = False
        return

    m  = (l + r) // 2
    ln = m - l + 1
    rn = r - m
    lc = node * 2
    rc = lc + 1

    if nd[4]:  # has_set
        v = nd[5]
        apply_set(seg, lc, ln, v)
        apply_set(seg, rc, rn, v)
        nd[4] = False

    if nd[3] != 0:
        v = nd[3]
        apply_add(seg, lc, ln, v)
        apply_add(seg, rc, rn, v)
        nd[3] = 0

    if nd[1] == nd[2]:
        v = nd[1]
        tgtL = [v * ln, v, v, 0, True, v]
        tgtR = [v * rn, v, v, 0, True, v]
        if seg[lc] != tgtL:
            apply_set(seg, lc, ln, v)
        if seg[rc] != tgtR:
            apply_set(seg, rc, rn, v)

def range_add(seg, node, l, r, ql, qr, v):
    if qr < l or r < ql:
        return
    if ql <= l and r <= qr:
        apply_add(seg, node, r - l + 1, v)
        return
    push(seg, node, l, r)
    m = (l + r) // 2
    range_add(seg, node * 2, l, m, ql, qr, v)
    range_add(seg, node * 2 + 1, m + 1, r, ql, qr, v)
    seg[node] = merge_node(seg[node * 2], seg[node * 2 + 1])

def range_sum(seg, node, l, r, ql, qr) -> int:
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return seg[node][0]
    push(seg, node, l, r)
    m = (l + r) // 2
    return range_sum(seg, node * 2, l, m, ql, qr) + range_sum(seg, node * 2 + 1, m + 1, r, ql, qr)

def try_collapse_set(seg, node, l, r) -> bool:
    nd = seg[node]
    mn = nd[1]
    mx = nd[2]
    if mx <= 1:
        return True

    if mn == mx:
        v = math.isqrt(mn)
        apply_set(seg, node, r - l + 1, v)
        return True

    tmin = math.isqrt(mn)
    tmax = math.isqrt(mx)
    if tmin == tmax and mn >= tmin * tmin and mx < (tmin + 1) * (tmin + 1):
        v = tmin
        apply_set(seg, node, r - l + 1, v)
        return True
    return False

def range_sqrt(seg, node, l, r, ql, qr):
    if qr < l or r < ql:
        return

    if ql <= l and r <= qr:
        if try_collapse_set(seg, node, l, r):
            return
        nd = seg[node]
        mn, mx = nd[1], nd[2]
        if mx == mn + 1:
            k_mn = math.isqrt(mn)
            k_mx = math.isqrt(mx)
            if k_mn != k_mx:
                delta = k_mn - mn
                apply_add(seg, node, r - l + 1, delta)
                return

    push(seg, node, l, r)
    if l == r:
        v = math.isqrt(seg[node][1])
        apply_set(seg, node, 1, v)
        return

    m  = (l + r) // 2
    lc = node * 2
    rc = lc + 1

    if ql <= l and m <= qr:
        if not try_collapse_set(seg, lc, l, m):
            range_sqrt(seg, lc, l, m, ql, qr)
    else:
        range_sqrt(seg, lc, l, m, ql, qr)

    if ql <= m + 1 and r <= qr:
        if not try_collapse_set(seg, rc, m + 1, r):
            range_sqrt(seg, rc, m + 1, r, ql, qr)
    else:
        range_sqrt(seg, rc, m + 1, r, ql, qr)

    seg[node] = merge_node(seg[lc], seg[rc])

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    seg = [[0, 0, 0, 0, False, 0] for _ in range(4 * n)]
    build(seg, arr, 1, 1, n)

    m = int(input().strip())
    out_lines = []
    for _ in range(m):
        parts = list(map(int, input().split()))
        t = parts[0]
        if t == 1:
            _, L, R, X = parts
            range_add(seg, 1, 1, n, L, R, X)
        elif t == 2:
            _, L, R = parts
            range_sqrt(seg, 1, 1, n, L, R)
        else:
            _, L, R = parts
            out_lines.append(str(range_sum(seg, 1, 1, n, L, R)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()