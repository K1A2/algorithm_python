n, m = map(int, input().split())

reslut = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_number = min(data)
    if reslut < min_number:
        reslut = min_number

print(reslut)