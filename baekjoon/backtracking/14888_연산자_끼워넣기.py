import sys
max_v = -1e10
min_v = 1e10
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
plus, minus, multi, div = map(int, sys.stdin.readline().rstrip().split())
def backtracking(plu, miu, mul, div, num, idx):
    if idx == n:
        global max_v, min_v
        max_v = max(max_v, num)
        min_v = min(min_v, num)
        return
    if plu > 0:
        backtracking(plu - 1, miu, mul, div, num + numbers[idx], idx + 1)
    if miu > 0:
        backtracking(plu, miu - 1, mul, div, num - numbers[idx], idx + 1)
    if mul > 0:
        backtracking(plu, miu, mul - 1, div, num * numbers[idx], idx + 1)
    if div > 0:
        if num < 0 and numbers[idx] > 0:
            backtracking(plu, miu, mul, div - 1, -(-num // numbers[idx]), idx + 1)
        else:
            backtracking(plu, miu, mul, div - 1, num // numbers[idx], idx + 1)
backtracking(plus, minus, multi, div, numbers[0], 1)
print(max_v)
print(min_v)