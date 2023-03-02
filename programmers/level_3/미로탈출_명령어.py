from collections import deque
def solution(n, m, x, y, r, c, k):
    dxy = ((-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'))
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    q = deque()
    q.append((x, y, k, ''))
    while q:
        qx, qy, qk, ans = q.pop()
        for d in dxy:
            nx = qx + d[0]
            ny = qy + d[1]
            nk = qk - 1
            nans = ans + d[-1]
            if 0 <= nx < n and 0 <= ny < m:
                if not nk and nx == r and ny == c:
                    return nans
                if nk % 2 and nx == r and ny == c:
                    return 'impossible'
                if nk > 0 and abs(nx - r) + abs(ny - c) <= nk:
                    q.append((nx, ny, nk, nans))
    return 'impossible'

testcase = [
    ([3, 4, 2, 3, 3, 1, 5], 'dllrl'),
    ([2, 2, 1, 1, 2, 2, 2], 'dr'),
    ([3, 3, 1, 2, 3, 3, 4], 'impossible'),
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(*t[0]) == t[-1]}')