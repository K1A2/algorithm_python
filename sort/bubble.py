import pickle
import time
with open('sort_data.pkl', 'rb') as f:
    random_list = pickle.load(f)
n = len(random_list)
print(random_list[:10])
print('Sorting Start')

start_time = time.perf_counter()

for i in range(n):
    for j in range(1, n - i):
        if random_list[j - 1] > random_list[j]:
            random_list[j], random_list[j - 1] = random_list[j - 1], random_list[j]

end_time = time.perf_counter()
print(f"실행 시간: {end_time - start_time:.5f}초")
