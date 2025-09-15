import heapq
import sys
input = sys.stdin.readline

n = int(input())
end_q = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    end_q.append((a, b))
end_q.sort(key=lambda x: (x[1], x[0]))
d = int(input())

s_q = []
ans = 0
for s, e, in end_q:
    if e - s <= d:
        heapq.heappush(s_q, s)
    else:
        continue

    while s_q:
        if e - s_q[0] > d:
            heapq.heappop(s_q)
        else:
            break

    ans = max(ans, len(s_q))
print(ans)
