import heapq
import sys
data = []
abs_count = dict()
for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    if num:
        if abs(num) in abs_count:
            heapq.heappush(abs_count[abs(num)], num)
        else:
            abs_count[abs(num)] = [num]
            heapq.heapify(abs_count[abs(num)])
            heapq.heappush(data, abs(num))
    else:
        if data:
            print(heapq.heappop(abs_count[data[0]]))
            if not abs_count[data[0]]:
                del abs_count[heapq.heappop(data)]
        else:
            print(0)