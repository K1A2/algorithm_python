n = int(input())
data = list(map(int, input().split()))
left = right = 0
count = dict()
ans = 0
while right < n:
    try:
        count[data[right]] += 1
    except:
        count[data[right]] = 1
    if len(count.keys()) > 2:
        count[data[left]] -= 1
        if count[data[left]] == 0:
            del count[data[left]]
        left += 1
    ans = max(ans, right - left + 1)
    right += 1
print(ans)
