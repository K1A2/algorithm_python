import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
datas = list(map(int, input().rstrip().split()))
datas.sort()
def backtracking(start, to, l, nums, m):
    if len(l) == m:
        print(*l)
        return
    for i in range(start, to):
        l.append(nums[i])
        backtracking(i, to, l, nums, m)
        l.pop()
backtracking(0, n, [], datas, m)