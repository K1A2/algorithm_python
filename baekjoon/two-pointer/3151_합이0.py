import sys
input = sys.stdin.readline
n = int(input())
data = sorted(list(map(int, input().split())))
res = 0
for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        target = data[right] + data[left]
        if target == -data[i]:
            if data[right] == data[left]:
                res += right - left
                left += 1
            else:
                j, k = left, right
                while data[j] == data[left] and j < right:
                    j += 1
                while data[k] == data[right] and k > left:
                    k -= 1
                res += (j - left) * (right - k)
                left, right = j, k
        elif target < -data[i]:
            left += 1
        else:
            right -= 1
print(res)
