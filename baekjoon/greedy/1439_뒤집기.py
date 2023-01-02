import re
a = input()
a = re.sub('1+', 'a', a)
a = re.sub('0+', 'b', a)
if a[0] == 'a' and a[-1] == 'a':
    print(a.count('a') - 1)
elif a[0] == 'a' and a[-1] != 'a':
    print(a.count('a'))
elif a[0] == 'b' and a[-1] == 'b':
    print(a.count('b') - 1)
elif a[0] == 'b' and a[-1] != 'b':
    print(a.count('b'))