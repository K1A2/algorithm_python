def backtracking(start, to, result, nums):
    if len(result) == 6:
        print(*result)
        return
    for i in range(start, to):
        result.append(nums[i])
        backtracking(i + 1, to, result, nums)
        result.pop()
while True:
    nums = input()
    if nums == '0': break
    nums = list(map(int, nums.split()))[1:]
    backtracking(0, len(nums), [], nums)
    print()