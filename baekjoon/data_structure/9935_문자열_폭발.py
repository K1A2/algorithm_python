import sys
strs, bomb = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
b_len = len(bomb)
q = []
for i in strs:
    q.append(i)
    q_len = len(q)
    if q_len >= b_len and ''.join(q[-b_len:]) == bomb:
        del q[-b_len:]
result = ''.join(q)
print(result if result else 'FRULA')