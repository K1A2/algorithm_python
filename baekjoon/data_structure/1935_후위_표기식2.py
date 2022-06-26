import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
cer = list(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]
d = deque()
for s in cer:
    if 'A' <= s <= 'Z':
        d.append(nums[ord(s) - ord('A')])
    else:
        a, b = d.pop(), d.pop()
        d.append(eval(f'{b}{s}{a}'))
print('%.2f' % (d.pop()))