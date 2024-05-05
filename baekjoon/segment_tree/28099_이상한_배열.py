import sys
input = lambda : sys.stdin.readline()

def init_tree(node, left, right):
    if left == right:
        tree[node] = values[left]
        return
    mid = (left + right) // 2
    init_tree(node * 2, left, mid)
    init_tree(node * 2 + 1, mid + 1, right)
    tree[node] = max(tree[node * 2], tree[node * 2 + 1])

def query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return max(query(node * 2, start, end, left, mid), query(node * 2 + 1, start, end, mid + 1, right))

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        values = list(map(int, input().split()))

        num_idx = dict()
        for i in range(n):
            v = values[i]
            try:
                num_idx[v].append(i)
            except:
                num_idx[v] = [i]

        tree = [0] * (4 * n)
        init_tree(1, 0, n - 1)
        flag = 1
        for v in num_idx.keys():
            if num_idx[v] is None or len(num_idx[v]) == 1:
                continue
            max_num = query(1, num_idx[v][0] + 1, num_idx[v][-1] + 1 - 1, 0, n - 1)
            if max_num > v:
                flag = 0
                break
        print('Yes' if flag else 'No')
