import sys
from collections import deque
num = ''
result = ''
stack = deque()
strs = sys.stdin.readline().rstrip()
new_strs = ''
pm = dict()
bracket_in = 0
for i in strs:
    if i =='*' or i == '/':
        if new_strs[-1] != ')':
            new_strs = new_strs[:-1] + '(' + new_strs[-1] + i
            if bracket_in in pm:
                pm[bracket_in] += 1
            else:
                pm[bracket_in] = 1
        else:
            back = -1
            count = 1
            for j in range(len(new_strs) - 2, -1, -1):
                if new_strs[j] == ')':
                    count += 1
                elif new_strs[j] == '(':
                    count -= 1
                    if count == 0:
                        back = j
                        break
            new_strs = new_strs[:back + 1] + '(' + new_strs[back + 1:] + i
            if bracket_in in pm:
                pm[bracket_in] += 1
            else:
                pm[bracket_in] = 1
    elif i == '(':
        new_strs += i
        bracket_in += 1
    elif i == ')':
        new_strs += i
        bracket_in -= 1
        while bracket_in in pm and pm[bracket_in]:
            new_strs += ')'
            pm[bracket_in] -= 1
    else:
        new_strs += i
        if bracket_in in pm and pm[bracket_in]:
            new_strs += ')'
            pm[bracket_in] -= 1
for i in new_strs:
    if i == '(':
        stack.append(i)
    elif i == '*' or i == '/':
        if num != '':
            result += num
            num = ''
        if stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        if num != '':
            result += num
            num = ''
        if stack and (stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-'):
            result += stack.pop()
        stack.append(i)
    elif i == ')':
        if num != '':
            result += num
            num = ''
        while True:
            if stack:
                if stack[-1] != '(':
                    result += stack.pop()
                else:
                    stack.pop()
                    break
            else:
                break
    else:
        num += i
if num != '':
    result += num
while stack:
    result += stack.pop()
print(result)