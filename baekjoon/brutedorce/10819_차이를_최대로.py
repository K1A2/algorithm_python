n = int(input())
data = list(map(int, input().split()))
available = [1] * n
ans = 0

def backtracking(prev, num, depth):
    global ans
    if depth == n:
        ans = max(ans, num)
        return
    for i in range(n):
        if not available[i]: continue
        available[i] = 0
        backtracking(data[i], num + abs(prev - data[i]), depth + 1)
        available[i] = 1

for i in range(n):
    available[i] = 0
    backtracking(data[i], 0, 1)
    available[i] = 1
print(ans)
