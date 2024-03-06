import sys
input = sys.stdin.readline
n, m = map(int, input().split())
truth_people = list(map(int, input().split()))
truth = truth_people[0]
del truth_people[0]

if truth == 0:
    print(m)
    exit()

parent = [i for i in range(n + 1)]
count = [0] * (n + 1)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, truth):
    union(truth_people[i - 1], truth_people[i])

for _ in range(m):
    party_people = list(map(int, input().split()))
    party = party_people[0]
    del party_people[0]

    count_party = 0
    count_target = set()
    count_target.add(find(party_people[0]))
    for i in range(1, party):
        count_target.add(find(party_people[i]))
        union(party_people[i - 1], party_people[i])
    for c in count_target:
        count_party += count[c]
    count[find(party_people[0])] = count_party + 1

print(m - count[find(truth_people[0])])
