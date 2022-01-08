from functools import cmp_to_key
data = []
for _ in range(int(input())):
    data.append(tuple(input().split()))
def nsort(a, b):
    aname, akr, aeng, amath = a
    bname, bkr, beng, bmath = b
    akr, aeng, amath = int(akr), int(aeng), int(amath)
    bkr, beng, bmath = int(bkr), int(beng), int(bmath)
    if akr < bkr:
        return 1
    elif akr > bkr:
        return -1
    else:
        if aeng < beng:
            return -1
        elif aeng > beng:
            return 1
        else:
            if amath < bmath:
                return 1
            elif amath > bmath:
                return -1
            else:
                for i in range(min([len(a), len(b)])):
                    if a[i] > b[i]:
                        return 1
                    elif a[i] < b[i]:
                        return -1
                if len(a) > len(b):
                    return 1
                elif len(a) < len(b):
                    return -1
                else:
                    return 0
for i in sorted(data, key=cmp_to_key(nsort)):
    print(i[0])