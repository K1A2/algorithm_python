from collections import deque
import sys
data = [[i, 0, 0, 0] for i in range(1, 101)]
ladder, snake = map(int, sys.stdin.readline().rstrip().split())
for _ in range(ladder):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data[a - 1] = (a, 1, b)
for _ in range(snake):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data[a - 1] = (a, 2, b)
que = deque()
que.append((1, 0))
while que:
    now, count = que.popleft()
    for i in range(1, 7):
        next = now + i
        if next == 100:
            print(count + 1)
            exit()
        elif next < 100:
            if data[next - 1][1] == 1:
                next = data[next - 1][2]
            elif data[next - 1][1] == 2:
                next = data[next - 1][2]
            if data[next - 1][3]:
                continue
            data[next - 1][3] = 1
            que.append((next, count + 1))