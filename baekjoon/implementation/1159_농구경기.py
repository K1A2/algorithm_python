import sys
input = sys.stdin.readline
count = [0] * 26
for _ in range(int(input())):
    count[ord(input()[0]) - 97] += 1
asw = ''
for idx, n in enumerate(count):
    if n >= 5:
        asw += chr(idx + 97)
if asw:
    print(asw)
else:
    print('PREDAJA')