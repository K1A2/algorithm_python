import sys
from collections import deque
data = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
stack = deque()
now = 0
result = ''
for i in range(1, max(data) + 1):
    if i < data[now]:
        stack.append(i)
        result += '+\n'
    else:
        if i == data[now]:
            stack.append(i)
            result += '+\n'
        while now < len(data) and len(stack) > 0 and data[now] == stack[len(stack) - 1]:
            stack.pop()
            result += '-\n'
            now += 1
if len(stack) != 0:
    print('NO')
else:
    print(result)