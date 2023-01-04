import sys
input = sys.stdin.readline
n = int(input())
minus = []
plus = []
for _ in range(n):
    a = int(input())
    if a > 0:
        plus.append(a)
    else:
        minus.append(a)
plus.sort()
minus.sort(reverse=True)
result = 0
while 1:
    if len(plus) > 1:
        result += max(plus[-1] * plus[-2], plus[-1] + plus[-2])
        plus.pop()
        plus.pop()
    else:
        break
while 1:
    if len(minus) > 1:
        result += max(minus[-1] * minus[-2], minus[-1] + minus[-2])
        minus.pop()
        minus.pop()
    else:
        break
if len(minus) > 0 and len(plus) > 0:
    result += max(minus[-1] * plus[-1], minus[-1] + plus[-1])
elif len(minus) > 0:
    result += minus[-1]
elif len(plus) > 0:
    result += plus[-1]
print(result)
