from collections import deque
for _ in range(int(input())):
    q = deque()
    isyes = True
    for i in input():
        if i == '(':
            q.append(i)
        else:
            if len(q) == 0:
                isyes = False
                break
            else:
                q.popleft()
    if isyes and len(q) == 0:
        print('YES')
    else:
        print('NO')