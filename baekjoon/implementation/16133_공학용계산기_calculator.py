import sys
from collections import deque
input = sys.stdin.readline
data = input().rstrip()
stack = deque()
infix_data = deque()
prev_number = ''
prior = {'#': 5, '^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
for d in data:
    if d.isdigit():
        prev_number += d
    else:
        infix_data.append(int(prev_number))
        prev_number = ''
        if d == '('
print(infix_data)
