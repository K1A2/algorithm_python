from collections import deque

for _ in range(int(input())):
    SIZE = int(input())
    visited = set()
    start = tuple(map(int, input().split()))
    to = tuple(map(int, input().split()))

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    queue = deque()
    queue.append((start[0], start[1], 0))

    while queue:
        x, y, count = queue.popleft()
        if x == to[0] and y == to[1]:
            print(count)
            break
        if (str(x) + ' ' + str(y)) in visited:
            continue
        visited.add(str(x) + ' ' + str(y))
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE and (str(nx) + ' ' + str(ny)) not in visited:
                queue.append((nx, ny, count + 1))