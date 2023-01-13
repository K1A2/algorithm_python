import re

def sub_symbol(l):
    return re.sub('&(lt|gt|amp);', '', l)

def sub_hex(l):
    return re.sub('&x([a-fA-F0-9]{2})+;', '', l)

def sub_check(l):
    return re.sub('<[a-z0-9]+>|</[a-z0-9]+>|<[a-z0-9]+/>', '', l)

def check_tag(l):
    tags = re.findall(r'<[a-z0-9]+>|</[a-z0-9]+>', l)
    stack = []
    for t in tags:
        if t[1] == '/':
            if not len(stack):
                return 0
            if stack[-1] == t[2:-1]:
                stack.pop()
        else:
            stack.append(t[1:-1])
    if len(stack) == 0:
        return 1
    else:
        return 0

def check_invalid(l):
    if re.search(r'(<|>|&)', l):
        return 1
    if re.sub('[ -\x7f]', '', l):
        return 1
    return 0

while 1:
    try:
        line = input()
        line = sub_symbol(line)
        line = sub_hex(line)
        if not check_tag(line):
            print('invalid')
            continue
        line = sub_check(line)
        if check_invalid(line):
            print('invalid')
        else:
            print('valid')
    except EOFError:
        break
