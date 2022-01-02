num = int(input())
k = 2
while num != 1:
    if num % k != 0:
        k += 1
        continue
    num //= k
    print(k)