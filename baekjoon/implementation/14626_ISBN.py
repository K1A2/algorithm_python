x = input()
a = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
c = 0
m = 0
for i in range(len(x)):
    if x[i] == '*':
        c = i
        continue
    m += a[i] * int(x[i])
r = (10 - m % 10) * (7 if a[c] == 3 else 1) % 10
print(r if r != 10 else 0)
