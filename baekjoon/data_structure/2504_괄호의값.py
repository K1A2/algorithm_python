from collections import deque
data = input()
q = deque()
n = deque()
for idx, i in enumerate(data):
    if i == '(' or i == '[':
        q.append((i, idx))
        n.append(i)
        continue

    if len(q) > 0 and ((q[-1][0] == '(' and i == ')') or (q[-1][0] == '[' and i == ']')):
        num = 2 if i == ')' else 3
        target = '(' if i == ')' else '['

        if len(n) > 0:
            if idx - q[-1][1] == 1:
                n.pop()
                n.append(num)
            else:
                s = 0
                while n[-1] != target:
                    s += n.pop()
                n.pop()
                n.append(s * num)
        else:
            n.append(num)
        q.pop()
    else:
        print(0)
        exit(0)
if len(q) > 0:
    print(0)
else:
    print(sum(n))
