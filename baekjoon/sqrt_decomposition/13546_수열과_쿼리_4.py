import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
data = list(map(int, input().split()))

query_inputs = []
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    query_inputs.append((i, a, b))
query_inputs.sort(key=lambda x: (x[1] // int(n ** 0.5), x[2]))

index_list = [deque([]) for _ in range(k + 1)]
max_distance = [0] * (k + 1)

ans = [''] * m
left = 0
right = -1
for i, a, b in query_inputs:
    a -= 1
    b -= 1

    while left > a:
        left -= 1
        index_list[data[left]].appendleft(left)
        if len(index_list[data[left]]) < 2:
            max_distance[data[left]] = 0
        else:
            max_distance[data[left]] = index_list[data[left]][-1] - index_list[data[left]][0]
    while right < b:
        right += 1
        index_list[data[right]].append(right)
        if len(index_list[data[right]]) < 2:
            max_distance[data[right]] = 0
        else:
            max_distance[data[right]] = index_list[data[right]][-1] - index_list[data[right]][0]
    while left < a:
        index_list[data[left]].popleft()
        if len(index_list[data[left]]) < 2:
            max_distance[data[left]] = 0
        else:
            max_distance[data[left]] = index_list[data[left]][-1] - index_list[data[left]][0]
        left += 1
    while right > b:
        index_list[data[right]].pop()
        if len(index_list[data[right]]) < 2:
            max_distance[data[right]] = 0
        else:
            max_distance[data[right]] = index_list[data[right]][-1] - index_list[data[right]][0]
        right -= 1
    ans[i] = f'{max(max_distance)}'
sys.stdout.write('\n'.join(ans))
