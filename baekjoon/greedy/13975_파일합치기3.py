import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    heapq.heapify(data)
    result = 0
    while len(data) > 1:
        a, b = heapq.heappop(data), heapq.heappop(data)
        result += a + b
        heapq.heappush(data, a + b)
    print(result)
