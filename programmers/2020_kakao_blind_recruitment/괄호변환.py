from collections import deque
balanced = 1
right = 2

def check_balance_right(s):
    q = deque()
    count_l = count_r = 0
    for i in s:
        if i == '(':
            q.append(i)
            count_l += 1
        else:
            if q:
                q.pop()
            count_r += 1
    if len(q) and count_l != count_r:
        return 0
    elif len(q) and count_l == count_r:
        return balanced
    elif not len(q) and count_l == count_r:
        return right

def calculate(s, res):
    if not s or check_balance_right(s) == right:
        return s
    for i in range(2, len(s) + 1, 2):
        u, v = s[:i], s[i:]
        u_type = check_balance_right(u)
        if u_type == right:
            res = calculate(v, res)
            return u + res
        elif u_type == balanced:
            n_str= '(' + calculate(v, res) + ')'
            u = u[1:-1]
            n_u = ''
            for j in u:
                n_u += '(' if j == ')' else ')'
            return n_str + n_u

def solution(p):
    return calculate(p, '')

print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))