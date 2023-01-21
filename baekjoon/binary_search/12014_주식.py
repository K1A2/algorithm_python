import sys
input = sys.stdin.readline

for ca in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    lis = [data[0]]

    for i in data:
        if lis[-1] < i:
            lis.append(i)
        else:
            start = 0
            end = len(lis) - 1
            while start <= end:
                mid = (start + end) // 2
                if lis[mid] == i:
                    start = mid
                    break
                if lis[mid] < i:
                    start = mid + 1
                else:
                    end = mid - 1
            lis[start] = i
    print(f'Case #{ca + 1}')
    print(int(len(lis) >= k))
