import sys
import math
from collections import deque
input = sys.stdin.readline
data = input().rstrip()
stack = deque()
infix_data = deque()
prev_number = ''
prior = {'#': 5, '^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
# prev_op = None
# i = 0
# while i < len(data) - 1:
#
for d in data[:-1]:
    if d.isdigit():
        prev_number += d
    else:
        if prev_number != '':
            infix_data.append(int(prev_number))
            prev_number = ''
        if d == '#':
            stack.append('#')
        elif d == '(':
            stack.append('(')
        elif d == ')':
            while stack[-1] != '(':
                infix_data.append(stack.pop())
            stack.pop()
            if stack and stack[-1] == '#':
                infix_data.append(stack.pop())
        else:
            if d == '#' and stack and stack[-1] == '#':
                stack.append('#')
            elif d == '^':
                idx = len(stack) - 1
                flag = 1
                while idx >= 0:
                    if prior[stack[idx]] < prior[d]:
                        break
                    flag = 0
                    idx -= 1
                if flag:
                    while stack and prior[d] <= prior[stack[-1]]:
                        infix_data.append(stack.pop())
                else:
                    while stack and prior[d] < prior[stack[-1]]:
                        infix_data.append(stack.pop())
                stack.append(d)
            else:
                while stack and prior[d] <= prior[stack[-1]]:
                    infix_data.append(stack.pop())
                stack.append(d)
if prev_number != '':
    infix_data.append(int(prev_number))
while stack:
    infix_data.append(stack.pop())
while infix_data:
    d = infix_data.popleft()
    if d == '#':
        ans = math.isqrt(stack.pop())
        if ans < 0: ans += 1
        stack.append(ans)
    elif d == '^':
        a, b = stack.pop(), stack.pop()
        stack.append(b ** a)
    elif d == '*':
        stack.append(stack.pop() * stack.pop())
    elif d == '/':
        a, b = stack.pop(), stack.pop()
        ans = b // a
        if ans < 0: ans += 1
        stack.append(ans)
    elif d == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    elif d == '+':
        stack.append(stack.pop() + stack.pop())
    else:
        stack.append(d)
print(stack.pop())
