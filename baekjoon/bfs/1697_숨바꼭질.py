from collections import deque

n, k = map(int, input().split())

count = 0
queue = deque()
queue.append([n])
visited = set()
while queue:
    q2 = queue.popleft()
    q = []
    while q2:
        now = q2.pop()
        if now in visited:
            continue
        visited.add(now)
        if now == k:
            print(count)
            exit()
        if now - 1 >= 0:
            q.append(now - 1)
        if now + 1 <= 100000:
            q.append(now + 1)
        if now * 2 <= 100000:
            q.append(now * 2)
    queue.append(q)
    count += 1