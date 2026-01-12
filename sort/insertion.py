import pickle
import time
with open('sort_data.pkl', 'rb') as f:
    data = pickle.load(f)
n = len(data)
print(data[:10])
print('Sorting Start')

start_time = time.perf_counter()

for i in range(1, n):
    number = data[i]
    idx = i - 1
    while idx >= 0 and data[idx] > number:
        data[idx + 1] = data[idx]
        idx -= 1
    data[idx + 1] = number

end_time = time.perf_counter()
print(data[:10])
print(f"실행 시간: {end_time - start_time:.5f}초")
