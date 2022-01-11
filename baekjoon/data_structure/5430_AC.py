from collections import deque
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    commands = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()[1:-1].split(',')
    if n > 0:
        data = deque(list(map(int, data)))
    else:
        data = deque()
    isok = True
    distance = 1
    for c in range(len(commands)):
        com = commands[c]
        if com == 'R':
            distance *= -1
        else:
            if data:
                if distance == -1:
                    data.pop()
                else:
                    data.popleft()
            else:
                sys.stdout.write('error\n')
                isok = False
                break
    if isok:
        if distance == -1:
            data.reverse()
        sys.stdout.write('[' + ','.join([str(i) for i in data]) + ']\n')