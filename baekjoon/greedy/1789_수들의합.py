num = int(input())
num_in = set()
now = 1
while num:
    if num < now:
        break
    num_in.add(now)
    num -= now
    now += 1
print(len(num_in))