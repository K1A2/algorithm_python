import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())


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
        self.segment_tree[node] = min(self.segment_tree[node * 2], self.segment_tree[node * 2 + 1])


    def query(self, node, strat, end, left, right):
        if right < strat or end < left:
            return 1
        if strat <= left and right <= end:
            return self.segment_tree[node]
        mid = (left + right) // 2
        return min(
            self.query(node * 2, strat, end, left, mid),
            self.query(node * 2 + 1, strat, end, mid + 1, right)
        )


    def path_query(self, u, v):
        min_val = 1

        while self.chain_head[u] != self.chain_head[v]:
            if self.depth[self.chain_head[u]] < self.depth[self.chain_head[v]]:
                u, v = v, u

            start_pos = self.position[self.chain_head[u]]
            end_pos = self.position[u]

            current_max = self.query(1, start_pos, end_pos, 1, self.size)
            min_val = min(min_val, current_max)

            u = self.parent[self.chain_head[u]]

        if self.depth[u] > self.depth[v]:
            u, v = v, u

        if u != v:
            start_pos = self.position[u] + 1
            end_pos = self.position[v]
            current_max = self.query(1, start_pos, end_pos, 1, self.size)
            min_val = min(min_val, current_max)

        return 'YES' if min_val else 'NO'


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
        self.segment_tree[node] = min(self.segment_tree[node * 2], self.segment_tree[node * 2 + 1])


    def update_edge(self, node, value):
        target_pos = self.position[node]
        self.update(1, 1, self.size, target_pos, value)



graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for i in range(1, n):
    p = int(input())
    graph[i + 1].append((p, 1))
    graph[p].append((i + 1, 1))
    parent[i + 1] = p

hld = HeavyLight(graph, parent, n)

for _ in range(q):
    a, b, i = map(int, input().split())
    if i == 1:
        res = hld.path_query(a, b)
        sys.stdout.write(f'{res}\n')
        if res == 'YES':
            hld.update_edge(a, 0)
        else:
            hld.update_edge(b, 0)
    elif i == 0:
        sys.stdout.write(f'{hld.path_query(a, b)}\n')
