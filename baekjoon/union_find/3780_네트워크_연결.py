import sys
input = sys.stdin.readline

def union(parent, a, b, line):
    parent[a] = b
    line[a] = abs(a - b) % 1000

def find(parent, a, line):
    if parent[a] != a:
        pa = find(parent, parent[a], line)
        line[a] += line[parent[a]]
        parent[a] = pa
    return parent[a]

for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)
    for i in range(n + 1):
        parent[i] = i

    line = [0] * (n + 1)
    while 1:
        i = input()
        if i == 'O': break
        i = i.split()
        if i[0] == 'E':
            find(parent, int(i[1]), line)
            print(line[int(i[1])])
        else:
            a, b = int(i[1]), int(i[2])
            union(parent, a, b, line)
