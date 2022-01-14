import sys
n = int(sys.stdin.readline().rstrip())
broken_len = int(sys.stdin.readline().rstrip())
broken = set(sys.stdin.readline().rstrip().split()) if broken_len != 0 else set()
if n == 100:
    print(0)
    exit()
if broken_len == 10:
    print(abs(n - 100))
    exit()
if broken == {'1','2','3','4','5','6','7','8','9'}:
    print(min(abs(n - 100), 1 + n))
    exit()
result = 100000000
minus = n + 1
plus = n
ok_m = ok_p = False
while not ok_m or not ok_p:
    if not ok_m:
        minus -= 1
        if minus < 0:
            ok_m = True
            continue
        ok_m = True
        for m in str(minus):
            if m in broken:
                ok_m = False
                break
        if ok_m:
            a = len(str(minus)) + n - minus
            if abs(100 - n) < a:
                a = abs(100 - n)
            result = min(result, a)
    if not ok_p:
        plus += 1
        ok_p = True
        for p in str(plus):
            if p in broken:
                ok_p = False
                break
        if ok_p:
            a = len(str(plus)) + plus - n
            if abs(n - 100) < a:
                a = abs(n - 100)
            result = min(result, a)
print(result)