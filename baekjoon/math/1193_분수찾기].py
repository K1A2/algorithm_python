i = int(input())
k = 1
s, s1 = 0, 0
while True:
    s, s1 = int(((k - 1) * (2 + (k - 2) * 1)) / 2), int((k * (2 + (k - 1) * 1)) / 2)
    if s < i <= s1:
        break
    k += 1
up = 1
down = k
now = s + 1
if k % 2 != 0:
    up = k
    down = 1
while now != i:
    if k % 2 != 0:
        up -= 1
        down += 1
    else:
        up += 1
        down -= 1
    now += 1
print(up,'/', down, sep='')