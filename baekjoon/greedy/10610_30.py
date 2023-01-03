a = sorted(list(map(int, list(input()))), reverse=True)
if a[-1] != 0:
    print(-1)
    exit()
if sum(a) % 3 == 0:
    print(''.join(map(str, a)))
else:
    print(-1)
