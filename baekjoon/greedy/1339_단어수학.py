import sys
input = sys.stdin.readline
n = int(input())
alpha_count = dict()
for _ in range(n):
    alphabets = input().rstrip()[::-1]
    for idx, s in enumerate(alphabets):
        if s in alpha_count:
            alpha_count[s] += 10 ** idx
        else:
            alpha_count[s] = 10 ** idx
data = sorted(alpha_count.values(), reverse=True)
result = 0
num = 9
for d in data:
    result += num * d
    num -= 1
print(result)
