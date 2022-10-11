a, b = map(int, input().split())
now = 0
data = [a]
while now not in data:
    if now: data.append(now)
    now = sum([int(i) ** b for i in str(data[-1])])
print(data.index(now))