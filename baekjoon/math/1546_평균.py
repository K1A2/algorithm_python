int(input())
socres = list(map(int, input().split()))
larger = max(socres)
all = 0
for i in socres:
    all += i / larger * 100
print(all / len(socres))