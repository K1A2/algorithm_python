strs = input()
res = ''
count = 0
for s in strs:
    if s == 'X':
        count += 1
    else:
        if not count % 2:
            res += 'AAAA' * (count // 4) + 'BB' * (count % 4 // 2)
            count = 0
        else:
            res = '-1'
            break
        res += s
if res != '-1':
    if not count % 2:
        res += 'AAAA' * (count // 4) + 'BB' * (count % 4 // 2)
    else:
        res = '-1'
print(res)