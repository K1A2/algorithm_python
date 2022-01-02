s = set()
for i in range(1, 10001):
    now = i
    while now <= 10000:
        now = now + sum(list(map(int, str(now))))
        s.add(now)
for i in range(1, 10001):
    if i not in s:
        print(i)