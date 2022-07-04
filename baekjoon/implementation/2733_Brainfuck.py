import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    print(f'PROGRAM #{i + 1}:')
    code = ''
    while 1:
        inp = input().rstrip()
        if inp == 'end': break
        com = inp.find('%')
        if com != -1:
            code += inp[:com]
        else:
            code += inp

    loop_pair = dict()
    len_code = len(code)
    d = deque()
    try:
        for k in range(len_code):
            if code[k] == '[':
                d.append(k)
            elif code[k] == ']':
                ls = d.pop()
                loop_pair[ls] = k
                loop_pair[k] = ls
    except:
        print('COMPILE ERROR')
        continue
    if d:
        print('COMPILE ERROR')
        continue

    m = 32768
    d.clear()
    memory = [0] * m
    pointer = now_bf = count = 0
    while now_bf < len_code:
        if code[now_bf] == '-':
            memory[pointer] -= 1
            if memory[pointer] == -1:
                memory[pointer] = 255
        elif code[now_bf] == '+':
            memory[pointer] += 1
            if memory[pointer] == 256:
                memory[pointer] = 0
        elif code[now_bf] == '<':
            pointer -= 1
            if pointer == -1:
                pointer = m - 1
        elif code[now_bf] == '>':
            pointer += 1
            if pointer == m:
                pointer = 0
        elif code[now_bf] == '[':
            if not memory[pointer]:
                now_bf = loop_pair[now_bf]
            else:
                d.append(now_bf)
        elif code[now_bf] == ']':
            if memory[pointer]:
                now_bf = loop_pair[now_bf]
            else:
                d.pop()
        elif code[now_bf] == '.':
            print(chr(memory[pointer]), end='')
        now_bf += 1
    print()