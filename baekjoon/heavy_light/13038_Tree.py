import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())


class HeavyLight:
    def __init__(self, graph, parent, size):
        self.size = size
        n = self.size + 1
        self.graph = graph

        self.parent = parent
        self.depth = [0] * n
        self.sub_size = [0] * n
        self.value = [0] * n
        self.heavy_child = [0] * n

        self.dfs1(1, 0)

        self.chain_head = [0] * n
        self.position = [0] * n
        self.pos_counter = 1
        self.dfs2(1, 1)

        self.arr = [0] * n
        for i in range(n):
            self.arr[self.position[i]] = self.value[i]
        self.segment_tree = [0] * (4 * self.size)
        self.init_tree(1, 1, self.size)


    def dfs1(self, node, depth):
        self.sub_size[node] = 1
        max_child_size = 0

        for child, weight in self.graph[node]:
            if child == self.parent[node]: continue

            # self.parent[child] = node
            self.depth[child] = depth + 1
            self.value[child] = weight

            child_count = self.dfs1(child, depth + 1)
            self.sub_size[node] += child_count
            if child_count > max_child_size:
                max_child_size = child_count
                self.heavy_child[node] = child

        return self.sub_size[node]


    def dfs2(self, node, group_parent):
        self.chain_head[node] = group_parent
        self.position[node] = self.pos_counter
        self.pos_counter += 1

        if self.heavy_child[node] != 0:
            self.dfs2(self.heavy_child[node], group_parent)

        for child, weight in self.graph[node]:
            if child == self.heavy_child[node] or child == self.parent[node]:
                continue
            self.dfs2(child, child)


    def init_tree(self, node, left, right):
        if left == right:
            self.segment_tree[node] = self.arr[left]
            return
        mid = (left + right) // 2
        self.init_tree(node * 2, left, mid)
        self.init_tree(node * 2 + 1, mid + 1, right)
        self.segment_tree[node] = self.segment_tree[node * 2] + self.segment_tree[node * 2 + 1]


    def query(self, node, strat, end, left, right):
        if right < strat or end < left:
            return 0
        if strat <= left and right <= end:
            return self.segment_tree[node]
        mid = (left + right) // 2
        return self.query(node * 2, strat, end, left, mid) +\
            self.query(node * 2 + 1, strat, end, mid + 1, right)


    def path_query(self, u, v):
        res = 0

        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u

            start_pos = self.position[self.chain_head[u]]
            end_pos = self.position[u]

            res += self.query(1, start_pos, end_pos, 1, self.size)

            u = self.parent[self.chain_head[u]]

        if self.depth[u] > self.depth[v]:
            u, v = v, u

        if u != v:
            start_pos = self.position[u] + 1
            end_pos = self.position[v]
            res += self.query(1, start_pos, end_pos, 1, self.size)

        return res


    def update(self, node, left, right, target_idx):
        if target_idx < left or right < target_idx:
            return
        if left == right:
            self.segment_tree[node] = 0
            return
        mid = (left + right) // 2
        if target_idx <= mid:
            self.update(node * 2, left, mid, target_idx)
        else:
            self.update(node * 2 + 1, mid + 1, right, target_idx)
        self.segment_tree[node] = self.segment_tree[node * 2] + self.segment_tree[node * 2 + 1]


    def update_edge(self, v):
        target_pos = self.position[v]
        self.update(1, 1, self.size, target_pos)


graph = [[] for _ in range(n + 1)]
parent = [0, 0] + list(map(int, input().split()))
for i in range(2, n + 1):
    graph[i].append((parent[i], 1))
    graph[parent[i]].append((i, 1))

hld = HeavyLight(graph, parent, n)

for _ in range(int(input())):
    i = list(map(int, input().split()))
    if i[0] == 2:
        _, v = i
        hld.update_edge(v)
    elif i[0] == 1:
        _, a, b = i
        sys.stdout.write(f'{hld.path_query(a, b)}\n')
