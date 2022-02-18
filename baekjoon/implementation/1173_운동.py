N, m, M, T, R = map(int, input().split())
res = time = 0
now = m
while time < N:
    if now + T > M:
        prev = now
        now = m if now - R < m else now - R
        if now == prev:
            res = -1
            break
    elif now + T <= M:
        now += T
        time += 1
    res += 1
print(res)