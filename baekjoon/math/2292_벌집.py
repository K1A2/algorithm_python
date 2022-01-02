i = int(input())
k = 0
if i == 1:
    print(1)
    exit(0)
while True:
    if 1 + (k * (12 + (k - 1) * 6)) / 2 < i <= 1 + ((k + 1) * (12 + (k) * 6)) / 2 :
        break
    k += 1
print(k + 2)