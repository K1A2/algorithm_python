max = int(input())

for i in range(0, max):
    l = input().split()
    max1 = l.pop(0)

    all = 0
    for iss in l:
        all += int(iss)
    mean = all / len(l)

    count = 0
    for isss in l:
        if int(isss) > mean:
            count +=1

    print(('%.3f' % round(count/len(l)*100, 3)) + "%")