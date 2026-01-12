import pickle
import time
with open('sort_data.pkl', 'rb') as f:
    random_list = pickle.load(f)
n = len(random_list)
print(random_list[:10])
print('Sorting Start')

start_time = time.perf_counter()

for i in range(n):
    idx = i
    for j in range(i + 1, n):
        if random_list[idx] > random_list[j]:
            idx = j
    random_list[idx], random_list[i] = random_list[i], random_list[idx]

end_time = time.perf_counter()
print(f"실행 시간: {end_time - start_time:.5f}초")
