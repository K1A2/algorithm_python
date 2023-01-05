import sys
input = sys.stdin.readline
n, k = int(input()), int(input())
sensors = sorted(list(set(map(int, input().split()))))
term = []
for i in range(len(sensors) - 1):
    term.append(sensors[i + 1] - sensors[i])
term.sort()
result = sum(term)
count = 0
while count < k - 1 and len(term):
    result -= term.pop()
    count += 1
print(result)
