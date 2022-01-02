n = int(input())
l = list(map(int, input().split()))
l.sort()
count = 0
for i in range(n):
    count += sum([l[j] for j in range(i + 1)])
print(count)