n = int(input())
result = 0
r = 1
for i in input():
    result += (ord(i) - ord('a') + 1) * r
    r *= 31
print(result % 1234567891)