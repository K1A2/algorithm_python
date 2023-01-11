import sys
from collections import deque
pattern = list(sys.stdin.readline().strip())
strs = sys.stdin.readline().strip()
p_len = len(pattern)
check_f = deque()
check_e = deque()
isf = -1
pos_f, pos_e = 0, len(strs) - 1
while pos_f <= pos_e:
    if isf == -1:
        check_f.append(strs[pos_f])
        len_cf = len(check_f)
        if len_cf >= p_len and [check_f[i] for i in range(len_cf - p_len, len_cf)] == pattern:
            for _ in range(p_len):
                check_f.pop()
            isf *= -1
        pos_f += 1
    else:
        check_e.appendleft(strs[pos_e])
        len_ce = len(check_e)
        if len_ce >= p_len and [check_e[i] for i in range(p_len)] == pattern:
            for _ in range(p_len):
                check_e.popleft()
            isf *= -1
        pos_e -= 1
while check_e:
    check_f.append(check_e.popleft())
    len_cf = len(check_f)
    if len_cf >= p_len and [check_f[i] for i in range(len_cf - p_len, len_cf)] == pattern:
        for _ in range(p_len):
            check_f.pop()
print(''.join(check_f))