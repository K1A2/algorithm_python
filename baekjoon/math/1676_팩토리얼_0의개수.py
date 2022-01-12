import math
count = 0
for i in str(math.factorial(int(input())))[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)