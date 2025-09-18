from typing import List
from dataclasses import dataclass
import sys
input = sys.stdin.readline

@dataclass
class Node:
    data: str
    children: List['Node']

root = Node(data='str', children=[])

for _ in range(int(input())):
    a = input().split()
    now = root
    for i in range(int(a[0])):
        find = 0
        for c in now.children:
            if c.data == a[i + 1]:
                now = c
                find = 1
                break
        if not find:
            new_node = Node(data=a[i + 1], children=[])
            now.children.append(new_node)
            now = new_node

def print_tree(node: Node, depth: int):
    if depth != -2:
        sys.stdout.write(f"{'-' * depth}{node.data}\n")
    if len(node.children) == 0:
        return
    node.children.sort(key=lambda a: a.data)
    for c in node.children:
        print_tree(c, depth + 2)

print_tree(root, -2)
