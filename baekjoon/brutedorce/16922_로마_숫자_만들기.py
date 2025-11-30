n = int(input())
numbers = [set() for _ in range(n)]


rome = (1, 5, 10, 50)
def backtracking(num, depth):
    if depth == n:
        return
    for i in rome:
        num += i
        if num in numbers[depth]:
            num -= i
            continue
        numbers[depth].add(num)
        backtracking(num, depth + 1)
        num -= i

backtracking(0, 0)
print(len(numbers[-1]))
