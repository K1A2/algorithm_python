from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

origin = input().rstrip().split('&&')
parent = []
dislike = []
value = dict()
key = dict()
set_number = dict()
idx = 0

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    int_idx = -1
    try:
        int(key[a])
        int_idx = 1
    except:
        pass
    try:
        int(key[b])
        int_idx = 2
    except:
        pass
    if int_idx == 1:
        parent[b] = a
    else:
        parent[a] = b

for o in origin:
    mode = 0
    a = o.split('==')
    if len(a) != 2:
        mode = 1
        a = o.split('!=')

    try:
        a_idx = value[a[0]]
    except:
        value[a[0]] = idx
        idx += 1
        a_idx = value[a[0]]
        key[a_idx] = a[0]
        parent.append(a_idx)
    try:
        b_idx = value[a[1]]
    except:
        value[a[1]] = idx
        idx += 1
        b_idx = value[a[1]]
        key[b_idx] = a[1]
        parent.append(b_idx)

    if mode == 0:
        if a[0] == a[1]:
            continue
        try:
            if int(key[find(value[a[0]])]) != int(key[find(value[a[1]])]):
                sys.stdout.write('0==1')
                exit()
        except SystemExit:
            raise
        except:
            pass
        union(a_idx, b_idx)
    else:
        try:
            if int(key[find(value[a[0]])]) == int(key[find(value[a[1]])]):
                sys.stdout.write('0==1')
                exit()
        except SystemExit:
            raise
        except:
            pass
        dislike.append((a_idx, b_idx))

small_parent = defaultdict(lambda : int(1e10))
sets = defaultdict(list)
for i in range(len(parent)):
    p = find(i)
    sets[p].append(i)
    try:
        if len(key[small_parent[p]]) > len(key[i]):
            small_parent[p] = i
    except:
        small_parent[p] = i

new_sets = defaultdict(list)
numbers = defaultdict(int)

ans = []
for k, v in small_parent.items():
    new_sets[v] = sets[k]
    try:
        int(key[k])
        numbers[v] = k
    except:
        pass
    for s in new_sets[v]:
        parent[s] = v
        if s == v: continue
        ans.append(f'{key[v]}=={key[s]}')

dis_check = set()
for dis_x, dis_y in dislike:
    if parent[dis_x] == parent[dis_y]:
        sys.stdout.write('0==1')
        exit()
    try:
        if int(key[numbers[parent[dis_x]]]) != int(key[numbers[parent[dis_y]]]):
            continue
    except:
        pass
    pair = (min(parent[dis_x], parent[dis_y]), max(parent[dis_x], parent[dis_y]))
    if pair in dis_check: continue
    ans.append(f'{key[parent[pair[0]]]}!={key[parent[pair[1]]]}')
    dis_check.add(pair)
if len(ans) == 0:
    sys.stdout.write('0==0')
else:
    sys.stdout.write('&&'.join(ans))
