b, c = [int(input()), int(input()), int(input())], [int(input()), int(input())]
small = 4001
for i in b:
    for j in c:
        if small > i + j:
            small = i + j
print(small - 50)