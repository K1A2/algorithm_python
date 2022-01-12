import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    if not a:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, a)