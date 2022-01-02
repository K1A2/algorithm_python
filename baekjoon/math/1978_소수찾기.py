n = []
input()
m = list(map(int, input().split()))
for i in m:
    if i == 1:
        continue
    isF = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            isF = False
            break
    if isF:
        n.append(i)
print(len(n))