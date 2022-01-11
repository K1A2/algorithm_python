from collections import deque
import sys
q = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'push_front':
        q.insert(0, int(com[1]))
    elif com[0] == 'push_back':
        q.append(int(com[1]))
    elif com[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif com[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])