l = [tuple(map(int, input().split())) for _ in range(int(input()))]
l = sorted(l, key=lambda x:x[0])
l = sorted(l, key=lambda x:x[1])
can = 0
last = 0
for times in l:
    if last <= times[0]:
        last = times[1]
        can += 1
print(can)