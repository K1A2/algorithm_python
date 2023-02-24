a, b = map(int, input().split())
len_a = len(str(a))
len_b = len(str(b))
if len_a != len_b :
    print(0)
else:
    asw = 0
    for i in range(len_a):
        if str(a)[i] != str(b)[i]: break
        if str(a)[i] == '8':
            asw += 1
    print(asw)