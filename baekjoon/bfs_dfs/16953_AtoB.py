from collections import deque
a, b = map(int, input().split())
que = deque()
que.append((a, 1))
while que:
    now, count = que.popleft()
    next_num = (int(str(now) + '1'), now * 2)
    for i in next_num:
        if i == b:
            print(count + 1)
            exit()
        elif i > b:
            continue
        que.append((i, count + 1))
print(-1)