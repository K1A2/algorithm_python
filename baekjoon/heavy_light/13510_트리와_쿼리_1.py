import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())


class HeavyLight:
    def __init__(self, graph, size):
        self.size = size
        n = self.size + 1
        self.graph = graph

        self.parent = [0] * n
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

        for pidx, child, weight in self.graph[node]:
            if child == self.parent[node]: continue

            self.parent[child] = node
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

        for pidx, child, weight in self.graph[node]:
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
        self.segment_tree[node] = max(self.segment_tree[node * 2], self.segment_tree[node * 2 + 1])


    def query(self, node, strat, end, left, right):
        if right < strat or end < left:
            return 0
        if strat <= left and right <= end:
            return self.segment_tree[node]
        mid = (left + right) // 2
        return max(
            self.query(node * 2, strat, end, left, mid),
            self.query(node * 2 + 1, strat, end, mid + 1, right)
        )


    def path_query(self, u, v):
        max_val = 0

        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u

            start_pos = self.position[self.chain_head[u]]
            end_pos = self.position[u]

            current_max = self.query(1, start_pos, end_pos, 1, self.size)
            max_val = max(max_val, current_max)

            u = self.parent[self.chain_head[u]]

        if self.depth[u] > self.depth[v]:
            u, v = v, u

        if u != v:
            start_pos = self.position[u] + 1
            end_pos = self.position[v]
            current_max = self.query(1, start_pos, end_pos, 1, self.size)
            max_val = max(max_val, current_max)

        return max_val


    def update(self, node, left, right, target_idx, value):
        if target_idx < left or right < target_idx:
            return
        if left == right:
            self.segment_tree[node] = value
            return
        mid = (left + right) // 2
        if target_idx <= mid:
            self.update(node * 2, left, mid, target_idx, value)
        else:
            self.update(node * 2 + 1, mid + 1, right, target_idx, value)
        self.segment_tree[node] = max(self.segment_tree[node * 2], self.segment_tree[node * 2 + 1])


    def update_edge(self, u, v, value):
        child_node = u
        if self.depth[u] < self.depth[v]:
            child_node = v
        target_pos = self.position[child_node]
        self.update(1, 1, self.size, target_pos, value)



graph = [[] for _ in range(n + 1)]
edge = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b, c = map(int, input().split())
    graph[a].append((i, b, c))
    graph[b].append((i, a, c))
    edge[i] = (a, b)

hld = HeavyLight(graph, n)

for _ in range(int(input())):
    i, a, b = map(int, input().split())
    if i == 1:
        hld.update_edge(edge[a][0], edge[a][1], b)
    elif i == 2:
        sys.stdout.write(f'{hld.path_query(a, b)}\n')
