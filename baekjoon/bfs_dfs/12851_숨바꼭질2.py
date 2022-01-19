from collections import deque
n, k = map(int, input().split())
time = 0
queue = deque()
queue.append([n])
visited = [[0, 0] for _ in range(100001)]
visited[n][1] = 1
while queue:
    q2 = queue.popleft()
    q = []
    for i in q2:
        if i == k:
            print(time)
            print(visited[i][1])
            exit()
    while q2:
        now = q2.pop()
        if now - 1 >= 0 and not visited[now - 1][0]:
            if not visited[now - 1][1]:
                q.append(now - 1)
            visited[now - 1][1] += visited[now][1]

        if now + 1 <= 100000 and not visited[now + 1][0]:
            if not visited[now + 1][1]:
                q.append(now + 1)
            visited[now + 1][1] += visited[now][1]

        if now * 2 <= 100000 and not visited[now * 2][0]:
            if not visited[now * 2][1]:
                q.append(now * 2)
            visited[now * 2][1] += visited[now][1]
    for i in q:
        visited[i][0] = 1
    queue.append(q)
    time += 1