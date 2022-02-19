h, m = map(int, input().split())
t = int(input())
if t >= 60:
    h += t // 60
    t %= 60
m += t
if m >= 60:
    m -= 60
    t += 1
    h += 1
if h >= 24:
    h -= 24
print(h, m)