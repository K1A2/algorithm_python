import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
query_update = []
query_print = []
i = 0
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        query_update.append(q)
    else:
        query_print.append(q + [i])
        i += 1
query_print.sort(key=lambda x: x[1])

tree = [0] * (4 * n)

def init(node, left, right):
    if left == right:
        tree[node] = data[left - 1]
        return
    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update(node, left, right, target, value):
    if left == right:
        tree[node] = value
        return
    mid = (left + right) // 2
    if target <= mid:
        update(node * 2, left, mid, target, value)
    else:
        update(node * 2 + 1, mid + 1, right, target, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return query(node * 2, start, end, left, mid) + \
        query(node * 2 + 1, start, end, mid + 1, right)

init(1, 1, n)

update_count = 0
print_idx = 0
ans = [0] * len(query_print)
while update_count < len(query_update) and print_idx < len(query_print):
    while query_print[print_idx][1] > update_count:
        _, t, v = query_update[update_count]
        update(1, 1, n, t, v)
        update_count += 1
    _, _, s, e, pi = query_print[print_idx]
    ans[pi] = str(query(1, s, e, 1, n))
    print_idx += 1
sys.stdout.write('\n'.join(ans))
