import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

def sub(left, right):
    sub_list = []
    for l in range(n):
        for r in range(n):
            sub_list.append(data[l][left] + data[r][right])
    return sub_list

sub_left = sub(0, 1)
sub_right = sub(2, 3)
sub_right.sort()
def find(target, arr, mode=0):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if mode == 0:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
    return left

ans = 0
for i in sub_left:
    target = -i
    ans += find(target, sub_right, 1) - find(target, sub_right)

print(ans)
