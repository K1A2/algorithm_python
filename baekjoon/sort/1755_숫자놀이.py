from functools import cmp_to_key
m, n = map(int, input().split())
change = {'0' : 'zero', '1': 'one', '2': 'tow', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
all = []
for i in range(m, n + 1):
    str_i = ''
    for j in str(i):
        str_i += change[j]
    all.append((str_i, i))
def nsort(a, b):
    a, b = a[0], b[0]
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
line = 0
for i in sorted(all, key=cmp_to_key(nsort)):
    print(i[1], end=' ')
    line += 1
    if line == 10:
        line = 0
        print()