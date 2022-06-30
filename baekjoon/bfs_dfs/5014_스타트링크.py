from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
deq = deque()
deq.append((s, 0))
visited[s] = 1
while deq:
    n, c = deq.popleft()
    if n == g:
        print(c)
        exit(0)
    if n - d > 0 and not visited[n - d]:
        visited[n - d] = 1
        deq.append((n - d, c + 1))
    if n + u <= f and not visited[n + u]:
        visited[n + u] = 1
        deq.append((n + u, c + 1))
print('use the stairs')