from collections import deque
import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == '.':
        break
    q = deque()
    checked = False
    for i in a:
        if i == '(':
            q.append('(')
        elif i == '[':
            q.append('[')
        elif i == ')':
            if len(q) == 0 or q[-1] != '(':
                print('no')
                checked = True
                break
            else:
                q.pop()
        elif i == ']':
            if len(q) == 0 or q[-1] != '[':
                print('no')
                checked = True
                break
            else:
                q.pop()
    if not checked:
        if len(q) == 0:
            print('yes')
        else:
            print('no')