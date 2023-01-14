import sys
from collections import deque
input = sys.stdin.readline

target = input().rstrip()
target_n = len(target)

data = deque(input().rstrip())
left = deque()
right = deque()

def slice(s, e, d):
    a = ''
    for i in range(s, e):
        a += d[i]
    return a

def compare_right():
    is_exe = 0
    while data:
        if len(right) >= target_n and slice(0, target_n, right) == target:
            for _ in range(target_n): right.popleft()
            is_exe = 1
            break
        right.appendleft(data.pop())
    if is_exe:
        return is_exe
    else:
        return compare_mid()

def compare_left():
    is_exe = 0
    while data:
        if len(left) >= target_n and slice(-target_n, 0, left) == target:
            for _ in range(target_n): left.pop()
            is_exe = 1
            break
        left.append(data.popleft())
    if is_exe:
        return is_exe
    else:
        return compare_mid()

def compare_mid():
    is_exe = 0
    while left:
        if len(right) >= target_n and slice(0, target_n, right) == target:
            for _ in range(target_n): right.popleft()
            is_exe = 1
            break
        right.appendleft(left.pop())
    return is_exe

def check_last(res):
    d = deque()
    if len(res) >= target_n:
        while res:
            if len(d) >= target_n and slice(0, target_n, d) == target:
                return 1
            d.appendleft(res.pop())
    return 0

count = 0
for _ in range(int(input())):
    is_exe = 0
    if data:
        if input().rstrip() == 'L':
            is_exe = compare_left()
        else:
            is_exe = compare_right()
    else:
        is_exe = compare_mid()
    count += is_exe
res = left + data + right
print(count)
print(''.join(res))
if check_last(res):
    print('You Lose!')
else:
    print('Perfect!')
