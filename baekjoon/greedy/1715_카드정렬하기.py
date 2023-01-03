import sys
from queue import PriorityQueue
input = sys.stdin.readline
q = PriorityQueue()
for _ in range(int(input())):
    q.put(int(input()))
result = 0
while len(q.queue) > 1:
    a, b = q.get(), q.get()
    result += a + b
    q.put(a + b)
print(result)
