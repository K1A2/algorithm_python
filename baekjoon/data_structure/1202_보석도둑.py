import sys
import heapq
n, k = map(int, sys.stdin.readline().rstrip().split())
data = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(data, (m, -v))
packs = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
packs.sort()
result = 0
check = []
for p in packs:
    while data and data[0][0] <= p:
        m, v = heapq.heappop(data)
        heapq.heappush(check, v)
    if check:
        result += -heapq.heappop(check)
print(result)