data = [0] * 12
data[1] = 1
data[2] = 2
data[3] = 4
def find(n):
    if data[n] != 0:
        return data[n]
    else:
        data[n] = find(n - 1) + find(n - 2) + find(n - 3)
        return data[n]
for _ in range(int(input())):
    print(find(int(input())))