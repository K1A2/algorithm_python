from collections import deque
s = input()
res = ''
q = deque()
is_in = 0
for i in s:
    if is_in:
        res += i
        if i == '>':
            is_in = 0
    else:
        if i == ' ':
            while q:
                res += q.pop()
            res += i
        elif i == '<':
            while q:
                res += q.pop()
            is_in = 1
            res += i
        else:
            q.append(i)
while q:
    res += q.pop()
print(res)