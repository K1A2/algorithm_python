import sys
input = sys.stdin.readline
gear = [list(map(int, input().rstrip())) for _ in range(4)]
spin = [[2, 6], [2, 6], [2, 6]]
for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1

    l = r = a
    l -= 1

    fl = fr = 0
    if r > 2: fr = 1
    if l < 0: fl = 1
    rotate = [0, 0, 0, 0]
    rotate[a] = b
    while 1:
        if not fl:
            if gear[l][spin[l][0]] != gear[l + 1][spin[l][1]]:
                rotate[l] = -rotate[l + 1]
                l -= 1
                if l < 0: fl = 1
            else:
                fl = 1
        if not fr:
            if gear[r][spin[r][0]] != gear[r + 1][spin[r][1]]:
                rotate[r + 1] = -rotate[r]
                r += 1
                if r > 2: fr = 1
            else:
                fr = 1

        if fl == fr == 1: break

    for i in range(4):
        if i - 1 >= 0:
            spin[i - 1][1] = (spin[i - 1][1] - rotate[i]) % 8
        if i < 3:
            spin[i][0] = (spin[i][0] - rotate[i]) % 8

res = 0
for i in range(4):
    c = ((spin[i][0] - 2) % 8) if i <= 2 else ((spin[i - 1][1] + 2) % 8)
    if gear[i][c] == 1:
        res += 2 ** i
print(res)
