a = list(input())
all = 0
number = ''
isminus = False
for i in a:
    if i == '-':
        if isminus:
            all -= int(number)
        else:
            all += int(number)
        number = ''
        isminus = True
    elif i == '+':
        if isminus:
            all -= int(number)
        else:
            all += int(number)
        number = ''
    else:
        number += i
if len(number) != 0:
    if isminus:
        all -= int(number)
    else:
        all += int(number)
    number = ''
print(all)