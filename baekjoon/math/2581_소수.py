start = int(input())
end = int(input())
l = []
if start == 1:
    start += 1
for i in range(start, end + 1):
    isR = True
    for j in range(2, (i // 2 + 1)):
        if i % j == 0:
            isR = False
            break
    if isR:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))