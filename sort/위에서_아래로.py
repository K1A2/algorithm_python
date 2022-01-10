l = []
for _ in range(int(input())):
    l.append(int(input()))
print(' '.join([str(i) for i in sorted(l)]))