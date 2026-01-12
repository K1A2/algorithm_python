import pickle
import time
import sys
sys.setrecursionlimit(int(1e6))

with open('sort_data.pkl', 'rb') as f:
    data = pickle.load(f)
n = len(data)
print(data[:10])
print('Sorting Start')


def merge(pdata, left, right, mid):
    data_left = pdata[left:mid + 1]
    data_right = pdata[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(data_left) and j < len(data_right):
        if data_left[i] < data_right[j]:
            pdata[k] = data_left[i]
            i += 1
        else:
            pdata[k] = data_right[j]
            j += 1
        k += 1

    while i < len(data_left):
        pdata[k] = data_left[i]
        i += 1
        k += 1

    while j < len(data_right):
        pdata[k] = data_right[j]
        j += 1
        k += 1

def sort(pdata, left, right):
    if left >= right: return
    mid = (left + right) // 2
    sort(pdata, left, mid)
    sort(pdata, mid + 1, right)
    merge(pdata, left, right, mid)


start_time = time.perf_counter()

sort(data, 0, n - 1)

end_time = time.perf_counter()
print(data[:10], data[-10:])
print(f"실행 시간: {end_time - start_time:.5f}초")
