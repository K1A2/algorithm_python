from functools import cmp_to_key
data = [input() for _ in range(int(input()))]
def nsort(x, y):
    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    else:
        a = b = 0
        for i in x:
            if '0' <= i <='9':
                a += int(i)
        for i in y:
            if '0' <= i <='9':
                b += int(i)
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            for i in range(len(x)):
                if x[i] > y[i]:
                    return 1
                elif x[i] < y[i]:
                    return -1
            return 0
print('\n'.join(sorted(data, key=cmp_to_key(nsort))))