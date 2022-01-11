from collections import deque
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    q = deque([(i, a[i]) for i in range(len(a))])
    count = 0
    while True:
        isok = True
        for i in range(1, len(q)):
            if q[0][1] < q[i][1]:
                isok = False
                break
        if isok:
            a = q.popleft()
            count += 1
            if a[0] == m:
                print(count)
                break
        else:
            q.append(q.popleft())