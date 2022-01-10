import time
import random
import copy
max_int = 1000
l = [random.randint(0, max_int) for _ in range(15000)]
def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    return l
def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break
    return l
def quick_sort(l):
    def quick_sort_in(l, start, end):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while left < right:
            while left <= end and l[left] <= l[pivot]:
                left += 1
            while right > start and l[right] >= l[pivot]:
                right -= 1
            if left > right:
                l[right], l[pivot] = l[pivot], l[right]
            else:
                l[left], l[right] = l[right], l[left]
        quick_sort_in(l, start, right - 1)
        quick_sort_in(l, right + 1, end)
    quick_sort_in(l, 0, len(l) - 1)
    return l
def merge_sort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    first_arr = merge_sort(l[:mid])
    second_arr = merge_sort(l[mid:])
    merged_arr = []
    f = s = 0
    while f < len(first_arr) and s < len(second_arr):
        if first_arr[f] < second_arr[s]:
            merged_arr.append(first_arr[f])
            f += 1
        else:
            merged_arr.append(second_arr[s])
            s += 1
    merged_arr += first_arr[f:]
    merged_arr += second_arr[s:]
    return merged_arr
def count_sort(l):
    count = [0] * (max_int + 1)
    for i in l:
        count[i] += 1
    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)
    return result

functions = [('선택정렬', selection_sort), ('삽입정렬', insertion_sort), ('퀵정렬', quick_sort),
             ('병합정렬', merge_sort), ('계수정렬', count_sort)]
for i in functions:
    q = copy.deepcopy(l)
    start = time.time()
    i[1](q)
    print(i[0] + ' 소요 시간:', time.time() - start, '초')