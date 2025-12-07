e, s, m = map(lambda x: int(x) - 1, input().split())
for i in range(1000000):
    if i % 15 == e and i % 28 == s and i % 19 == m:
        print(i + 1)
        exit()
