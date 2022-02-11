n = int(input())
res = list(input())
for _ in range(n - 1):
    now = input()
    for i in range(len(now)):
        if res[i] != now[i]:
            res[i] = '?'
print(''.join(res))