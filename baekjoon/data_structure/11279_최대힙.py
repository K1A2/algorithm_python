import sys
import heapq
h = []
for i in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    if num:
        heapq.heappush(h, (-num, num))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)