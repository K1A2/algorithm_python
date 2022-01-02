i = input()
check = int(i)
count = 0
while True:
    if len(i) <= 1:
        i = '0' + i
    d = str(int(i[0]) + int(i[1]))
    if len(d) == 2:
        d = d[1]
    i = i[1] + d
    count += 1
    if check == int(i):
        break
print(count)