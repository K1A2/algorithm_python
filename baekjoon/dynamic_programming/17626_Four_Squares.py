import math
n = int(input())
save = [0] * (n + 1)
if n < 4:
    print(n)
    exit()
save[1] = 1
save[2] = 2
save[3] = 3
def find(n):
    if n < 4:
        return save[n]
    sq = int(math.sqrt(n))
    for i in range(sq, 0, -1):
        if save[n - i ** 2] == 0:
            save[n - i ** 2] = find(n - i ** 2)
        if save[n] == 0:
            save[n] = 1 + save[n - i ** 2]
        else:
            save[n] = min(save[n], 1 + save[n - i ** 2])
    return save[n]
print(find(n))