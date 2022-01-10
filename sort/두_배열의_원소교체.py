n, k = map(int, input().split())
a = [i for i in map(int, input().split())]
b = [i for i in map(int, input().split())]
a.sort()
b.sort(reverse=True)
i = 0
while i < k:
    a[i], b[i] = b[i], a[i]
    i += 1
print(sum(a))