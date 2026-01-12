import pickle
import time
import sys
sys.setrecursionlimit(int(1e6))

with open('sort_data.pkl', 'rb') as f:
    data = pickle.load(f)
n = len(data)
print(data[:10])
print('Sorting Start')

min_heap = []

def insert(heap: list, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0 and heap[index] < heap[(index - 1) // 2]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2

def delete(heap: list):
    if len(heap) == 0: return -1

    if len(heap) == 1:
        return heap.pop()

    root_value = heap[0]

    heap[0] = heap.pop()
    index = 0
    while 1:
        smallest = index
        left_child = index * 2 + 1
        right_child = index * 2 + 2

        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child
        if smallest == index: break

        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest

    return root_value


start_time = time.perf_counter()

for i in data:
    insert(min_heap, i)

for j in range(len(data)):
    data[j] = delete(min_heap)

end_time = time.perf_counter()
print(data[:10], data[-10:])
print(f"실행 시간: {end_time - start_time:.5f}초")
