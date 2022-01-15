import sys
from collections import deque
dslr = [(lambda x:2 * x % 10000, 'D'), (lambda x:x - 1 if x > 0 else 9999, 'S'), (lambda x:x[1:] + x[0], 'L'), (lambda x:x[-1] + x[:-1], 'R')]
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = [0] * 10000
    q = deque()
    q.append((a, ''))
    visited[a] = 1
    while q:
        now, commands = q.popleft()
        for i in range(len(dslr)):
            new = int(dslr[i][0](now if i < 2 else str(now).zfill(4)))
            if visited[new]:
                continue
            visited[new] = 1
            if new == b:
                sys.stdout.write(f'{commands + dslr[i][1]}\n')
                q.clear()
                break
            q.append((new, commands + dslr[i][1]))