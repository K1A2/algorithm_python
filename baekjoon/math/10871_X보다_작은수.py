a, b = list(map(int, input().split()))
k = list(map(int, input().split()))
for i in range(a):
    if k[i] < b:
        print(k[i], end=" ")