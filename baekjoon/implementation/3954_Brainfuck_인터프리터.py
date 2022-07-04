import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    m, c, i = map(int, input().rstrip().split())
    brainfuck = input().rstrip()
    input_words = input().rstrip()

    loop_pair_s = dict()
    loop_pair_e = dict()
    d = deque()
    for k in range(c):
        if brainfuck[k] == '[':
            d.append(k)
        elif brainfuck[k] == ']':
            ls = d.pop()
            loop_pair_s[ls] = k
            loop_pair_e[k] = ls

    d.clear()
    memory = [0] * m
    pointer = input_idx = now_bf = count = 0
    is_loop = 1
    max_execute = 50000000
    min_idx = c
    while count < max_execute:
        if brainfuck[now_bf] == '-':
            memory[pointer] -= 1
            if memory[pointer] == -1:
                memory[pointer] = 255
        elif brainfuck[now_bf] == '+':
            memory[pointer] += 1
            if memory[pointer] == 256:
                memory[pointer] = 0
        elif brainfuck[now_bf] == '<':
            pointer -= 1
            if pointer == -1:
                pointer = m - 1
        elif brainfuck[now_bf] == '>':
            pointer += 1
            if pointer == m:
                pointer = 0
        elif brainfuck[now_bf] == '[':
            if not memory[pointer]:
                now_bf = loop_pair_s[now_bf]
            else:
                d.append(now_bf)
        elif brainfuck[now_bf] == ']':
            if memory[pointer]:
                now_bf = loop_pair_e[now_bf]
            else:
                d.pop()
        elif brainfuck[now_bf] == ',':
            if input_idx < i:
                memory[pointer] = ord(input_words[input_idx])
                input_idx += 1
            else:
                memory[pointer] = 255
        count += 1
        now_bf += 1
        if now_bf == c:
            is_loop = 0
            print('Terminates')
            break
        if count > 50000000:
            min_idx = min(min_idx, now_bf)
        if count == max_execute and is_loop:
            max_execute = 100000000
    if is_loop:
        min_idx -= 1
        print(f'Loops {min_idx} {loop_pair_s[min_idx]}')
