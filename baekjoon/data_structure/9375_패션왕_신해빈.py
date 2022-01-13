import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    col = dict()
    asw = 1
    for _ in range(int(sys.stdin.readline().rstrip())):
        i = sys.stdin.readline().rstrip().split()
        if i[1] in col:
            col[i[1]] += 1
        else:
            col[i[1]] = 1
    for i in col.values():
        asw *= i + 1
    asw -= 1
    sys.stdout.write(str(asw) + '\n')