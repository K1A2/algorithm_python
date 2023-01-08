import sys
from dataclasses import dataclass
input = sys.stdin.readline
free_size = 100000

@dataclass
class Node:
    right: 'Node' = None
    start: int = 0
    size: int = 0

def get_key(name):
    k = 0
    for i in range(4):
        k = k * 26 + (ord(name[i]) - ord('a'))
    return k

memory_free = Node()
memory_init = Node(start=1, size=free_size)
memory_free.right = memory_init
memory_alloc = [0] * (26 * 26 * 26 * 26)

for _ in range(int(input())):
    data = input().rstrip()
    if data[:5] == 'print':
        key = get_key(data[6:-2])
        if memory_alloc[key] == 0:
            print(0)
        else:
            print(memory_alloc[key].start)
    elif data[:4] == 'free':
        name = data[5:-2]
        key = get_key(name)
        memory_target = memory_alloc[key]
        if memory_target == 0:
            continue
        memory_now = memory_free
        free_size += memory_target.size
        if memory_now.right is None:
            memory_now.right = memory_target
            continue
        while memory_now.right:
            if memory_target.start + memory_target.size < memory_now.right.start:
                memory_target.right = memory_now.right
                memory_now.right = memory_target
                break
            memory_now = memory_now.right
            if memory_target.start + memory_target.size == memory_now.start:
                memory_now.start = memory_target.start
                memory_now.size += memory_target.size
                break
            if memory_target.start == memory_now.start + memory_now.size:
                memory_now.size += memory_target.size
                if memory_now.right is not None and (memory_now.right.start == memory_now.start + memory_now.size):
                    memory_now.size += memory_now.right.size
                    memory_now.right = memory_now.right.right
                break
        memory_alloc[key] = 0
    else:
        key = get_key(data[:4])
        size = int(data[12:-2])
        memory_now = memory_free
        if free_size < size:
            memory_alloc[key] = 0
            continue
        free_check = free_size
        not_alloc = 1
        while memory_now.right and free_check >= size:
            if memory_now.right.size == size:
                new_alloc = memory_now.right
                memory_now.right = new_alloc.right
                new_alloc.right = None
                free_size -= size
                memory_alloc[key] = new_alloc
                not_alloc = 0
                break
            if memory_now.right.size > size:
                new_alloc = Node(start=memory_now.right.start, size=size)
                memory_now.right.start += size
                memory_now.right.size -= size
                free_size -= size
                memory_alloc[key] = new_alloc
                not_alloc = 0
                break
            free_check -= memory_now.right.size
            memory_now = memory_now.right
        if not_alloc:
            memory_alloc[key] = 0
