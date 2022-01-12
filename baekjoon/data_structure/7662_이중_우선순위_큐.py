import heapq
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    data1 = []
    data2 = []
    visited = [0 for _ in range(1000001)]
    for i in range(int(sys.stdin.readline().rstrip())):
        com = sys.stdin.readline().rstrip().split()
        if com[0] == 'I':
            num = int(com[1])
            heapq.heappush(data1, (num, i))
            heapq.heappush(data2, (-num, i))
            visited[i] = 1
        else:
            if com[1] == '-1':
                while data1 and not visited[data1[0][1]]:
                    heapq.heappop(data1)
                if data1:
                    visited[data1[0][1]] = 0
                    heapq.heappop(data1)
            else:
                while data2 and not visited[data2[0][1]]:
                    heapq.heappop(data2)
                if data2:
                    visited[data2[0][1]] = 0
                    heapq.heappop(data2)
    while data1 and not visited[data1[0][1]]:
        heapq.heappop(data1)
    while data2 and not visited[data2[0][1]]:
        heapq.heappop(data2)
    if data1:
        sys.stdout.write(f'{-data2[0][0]} {data1[0][0]}\n')
    else:
        sys.stdout.write('EMPTY\n')