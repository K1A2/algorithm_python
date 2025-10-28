import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())


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
        self.lazy = [0] * (4 * self.size)
        self.init_tree(1, 1, self.size)


    def dfs1(self, node, depth):
        visited = {node}
        self.parent[node] = 0
        self.depth[node] = depth

        order = [1]
        head = 0
        while head < len(order):
            node = order[head]
            head += 1
            for child, weight in self.graph[node]:
                if child != self.parent[node]:
                    visited.add(child)
                    self.parent[child] = node
                    self.depth[child] = self.depth[node] + 1
                    self.value[child] = weight
                    order.append(child)

        for node in reversed(order):
            self.sub_size[node] = 1
            max_child_size = 0
            p_node = self.parent[node]

            for child, weight in self.graph[node]:
                if child != p_node:
                    self.sub_size[node] += self.sub_size[child]
                    if self.sub_size[child] > max_child_size:
                        max_child_size = self.sub_size[child]
                        self.heavy_child[node] = child


    def dfs2(self, node, group_parent):
        stack = deque([(node, group_parent)])

        while stack:
            node, head = stack.pop()

            self.chain_head[node] = head
            self.position[node] = self.pos_counter
            self.pos_counter += 1

            p_node = self.parent[node]
            heavy = self.heavy_child[node]

            for child, weight in reversed(self.graph[node]):
                if child != p_node and child != heavy:
                    stack.append((child, child))

            if heavy != 0:
                stack.append((heavy, head))


    def init_tree(self, node, left, right):
        if left == right:
            self.segment_tree[node] = self.arr[left]
            return
        mid = (left + right) // 2
        self.init_tree(node * 2, left, mid)
        self.init_tree(node * 2 + 1, mid + 1, right)
        self.segment_tree[node] = self.segment_tree[node * 2] + self.segment_tree[node * 2 + 1]


    def propagate(self, node, left, right):
        if self.lazy[node] == 0:
            return
        self.segment_tree[node] += (right - left + 1) * self.lazy[node]
        if left != right:
            self.lazy[node * 2] += self.lazy[node]
            self.lazy[node * 2 + 1] += self.lazy[node]
        self.lazy[node] = 0


    def query(self, node, strat, end, left, right):
        if right < strat or end < left:
            return 0
        self.propagate(node, left, right)
        if strat <= left and right <= end:
            return self.segment_tree[node]
        mid = (left + right) // 2
        return self.query(node * 2, strat, end, left, mid) + \
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


    def update(self, node, start, end, left, right):
        if end < left or right < start:
            return
        self.propagate(node, left, right)
        if start <= left and right <= end:
            self.lazy[node] += 1
            self.propagate(node, left, right)
            return
        mid = (left + right) // 2
        self.update(node * 2, start, end, left, mid)
        self.update(node * 2 + 1, start, end, mid + 1, right)
        self.segment_tree[node] = self.segment_tree[node * 2] + self.segment_tree[node * 2 + 1]


    def update_edge(self, u, v):
        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u
            start_pos = self.position[self.chain_head[u]]
            end_pos = self.position[u]
            self.update(1, start_pos, end_pos, 1, self.size)
            u = self.parent[self.chain_head[u]]

        if self.depth[u] > self.depth[v]:
            u, v = v, u

        if u != v:
            start_pos = self.position[u] + 1
            end_pos = self.position[v]
            self.update(1, start_pos, end_pos, 1, self.size)



graph = [[] for _ in range(n + 1)]
for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append((b, 0))
    graph[b].append((a, 0))

hld = HeavyLight(graph, n)

for _ in range(q):
    i, a, b = input().split()
    a, b = int(a), int(b)
    if i == 'P':
        hld.update_edge(a, b)
    elif i == 'Q':
        sys.stdout.write(f'{hld.path_query(a, b)}\n')
