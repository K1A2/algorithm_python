n = int(input())
data = input()
MIN = 1
MAX = 641
idx = n
count = 0
while idx > 0:
    if idx >= 3 and data[idx - 3] != '0' and int(data[idx - 3:idx]) <= MAX:
        count += 1
        idx -= 3
        continue
    if idx >= 2 and data[idx - 2] != '0' and int(data[idx - 2:idx]) <= MAX:
        count += 1
        idx -= 2
        continue
    count += 1
    idx -= 1
print(count)
