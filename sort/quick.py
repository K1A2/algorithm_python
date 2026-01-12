import pickle
import time
import sys
sys.setrecursionlimit(int(1e6))

with open('sort_data.pkl', 'rb') as f:
    data = pickle.load(f)
n = len(data)
print(data[:10])
print('Sorting Start')


def partition(pdata, left, right):
    pivot = pdata[left]
    low = left
    high = right
    while low < high:
        while low < high and pdata[high] > pivot:
            high -= 1
        while low < high and pdata[low] <= pivot:
            low += 1
        pdata[low], pdata[high] = pdata[high], pdata[low]
    pdata[left], pdata[low] = pdata[low], pdata[left]
    return low

def sort(pdata, left, right):
    if left >= right: return
    pivot_idx = partition(pdata, left, right)
    sort(pdata, left, pivot_idx - 1)
    sort(pdata, pivot_idx + 1, right)


start_time = time.perf_counter()

sort(data, 0, n - 1)

end_time = time.perf_counter()
print(data[:10], data[-10:])
print(f"실행 시간: {end_time - start_time:.5f}초")
