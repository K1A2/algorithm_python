import math
a = input()
count = [0] * 10
for i in a:
    if i == '9':
        i = '6'
    count[int(i)] += 1
count[6] = math.ceil(count[6] / 2)
print(max(count))
