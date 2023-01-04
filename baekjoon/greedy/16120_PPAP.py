from collections import deque
a = deque(input())
b = deque()
while len(a) > 0:
    b.append(a.popleft())
    if len(b) >= 4 and b[-1] == 'P' and b[-2] == 'A' and b[-3] == 'P' and b[-4] == 'P':
        for _ in range(4): b.popleft()
        b.append('P')
if list(b) == ['P']:
    print('PPAP')
else:
    print('NP')