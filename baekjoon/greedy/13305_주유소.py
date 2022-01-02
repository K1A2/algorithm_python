import sys
from sys import stdin
nodes = [[0, 0] for _ in range(int(stdin.readline()) - 1)] # [가격, 길이]
c = 0
for i in list(map(int, stdin.readline().rstrip().split())):
    nodes[c][1] = i
    c += 1
c = 0
for i in list(map(int, stdin.readline().rstrip().split())):
    nodes[c][0] = i
    if c == len(nodes) - 1:
        break
    c += 1
now_index = 0
last_price = 0
total = 0
while now_index != len(nodes):
    if not now_index:
        total += nodes[now_index][0] * nodes[now_index][1]
        last_price = nodes[now_index][0]
        now_index += 1
        continue
    if nodes[now_index][1] * last_price > nodes[now_index][1] * nodes[now_index][0]:
        last_price = nodes[now_index][0]
    total += nodes[now_index][1] * last_price
    now_index += 1
print(total)