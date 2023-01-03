from queue import PriorityQueue
import sys
input = sys.stdin.readline
data = [list(map(int, input().split())) for _ in range(int(input()))]
data = sorted(data, key=lambda x: (x[0], x[1]))
q = PriorityQueue()
result = 0
for i in data:
    t_in, t_out = i
    if len(q.queue) > 0 and q.queue[0] <= t_in:
        q.get()
        q.put(t_out)
    else:
        q.put(t_out)
        result += 1
print(result)
