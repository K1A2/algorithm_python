n, m = map(int, input().split())
data = list(map(int, input().split()))
start = 0
end = m - 1
s = sum(data[start:end + 1])
ans = s
while end < n - 1:
    s = s - data[start] + data[end + 1]
    ans = max(s, ans)
    start += 1
    end += 1
print(ans)
