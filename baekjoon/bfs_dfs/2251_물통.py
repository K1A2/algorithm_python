from collections import deque
bottles_size = tuple(map(int, input().split()))
que = deque()
que.append((0, 0, bottles_size[2]))
rsult = set()
rsult.add(bottles_size[2])
case = []
while que:
    bottles = que.popleft()
    for i in range(3):
        if not bottles[i]:
            continue
        for j in range(3):
            if i == j: continue
            new = list(bottles)
            if new[j] < bottles_size[j]:
                new[j] += new[i]
                if new[j] > bottles_size[j]:
                    new[i] = new[j] - bottles_size[j]
                    new[j] = bottles_size[j]
                else:
                    new[i] = 0
                if new not in case:
                    if new[0] == 0:
                        if new[2] not in rsult:
                            rsult.add(new[2])
                            que.append(new)
                            case.append(new)
                    else:
                        que.append(new)
                        case.append(new)
rsult = list(rsult)
rsult.sort()
print(' '.join(map(str, rsult)))