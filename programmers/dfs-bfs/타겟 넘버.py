sign = [-1, 1]
def dfs(now, numbers, count, target, depth):
    if depth == len(numbers):
        if now == target:
            return count + 1
        else:
            return count
    for s in sign:
        count = dfs(now + numbers[depth] * s, numbers, count, target, depth + 1)
    return count

def solution(numbers, target):
    return dfs(0, numbers, 0, target, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))