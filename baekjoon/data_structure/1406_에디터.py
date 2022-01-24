import sys
from collections import deque
strs = sys.stdin.readline().rstrip()
c1, c2 = deque(strs), deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == 'P':
        c1.append(commands[1])
    elif commands[0] == 'B':
        if c1:
            c1.pop()
    elif commands[0] == 'L':
        if c1:
            c2.appendleft(c1.pop())
    else:
        if c2:
            c1.append(c2.popleft())
print(''.join(c1 + c2))