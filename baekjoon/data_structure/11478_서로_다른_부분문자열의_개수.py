a = input()
res = set()
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        res.add(a[i:j])
print(len(res))