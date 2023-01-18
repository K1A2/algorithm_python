from collections import deque
n, k = map(int, input().split())
time = 0
queue = deque()
queue.append((n, 0))
visited = [0] * 100001
move = [0] * 100001
visited[n] = 1
move[n] = -1
while queue:
    now, time = queue.popleft()
    if now == k:
        print(time)
        path = str(now)
        while move[now] != -1:
            path = f'{move[now]} ' + path
            now = move[now]
        print(path)
        break
    for d in [now - 1, now + 1, now * 2]:
        if 0 <= d <= 100000 and not visited[d]:
            queue.append((d, time + 1))
            move[d] = now
            visited[d] = 1
