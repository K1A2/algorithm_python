from collections import deque

prime = [1] * 10000
prime[0] = prime[1] = 0
for i in range(2, int(10000 ** (1 / 2)) + 1):
    for j in range(i * 2, 10000, i):
        prime[j] = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, 0))
    visited = [0] * 10000
    visited[a] = 1
    found = 0
    while q:
        now, count = q.popleft()
        if now == b:
            print(count)
            found = 1
            break
        num = list(str(now))
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: continue
                if int(num[i]) == int(j): continue
                new_num = int(''.join(num[:i] + [str(j)] + num[i + 1:]))
                if prime[new_num] and visited[new_num] == 0:
                    visited[new_num] = 1
                    q.append((new_num, count + 1))
    if not found: print('Impossible')
