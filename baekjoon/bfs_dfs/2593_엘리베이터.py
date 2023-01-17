import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
elv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())
visited = [0] * (n + 1)

if min([i[0] for i in elv]) > t:
    print(-1)
    exit()

qeue = deque()
qeue.append((s, 0, ''))
visited[s] = 1
while qeue:
    now, c, log = qeue.popleft()
    for idx, e in enumerate(elv):
        elv_s, elv_d = e
        if (now - elv_s) % elv_d == 0:
            d = ((now - elv_s) // elv_d) - 1
            while d >= 0:
                if not visited[elv_s + d * elv_d]:
                    n_floor = elv_s + d * elv_d
                    if n_floor == t:
                        print(c + 1)
                        print(log + f'{idx + 1}\n')
                        exit()
                    qeue.append((n_floor, c + 1, log + f'{idx + 1}\n'))
                    visited[n_floor] = 1
                d -= 1
            d = ((now - elv_s) // elv_d) + 1
            while elv_s + d * elv_d <= n:
                if not visited[elv_s + d * elv_d]:
                    n_floor = elv_s + d * elv_d
                    if n_floor == t:
                        print(c + 1)
                        print(log + f'{idx + 1}\n')
                        exit()
                    qeue.append((n_floor, c + 1, log + f'{idx + 1}\n'))
                    visited[n_floor] = 1
                d += 1
print(-1)
