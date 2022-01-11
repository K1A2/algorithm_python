from collections import deque
import sys
q = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'push':
        q.append(int(com[1]))
    elif com[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])