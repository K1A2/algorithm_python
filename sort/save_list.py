import pickle
import random

my_list = random.sample(range(25000), 25000)
print(f"리스트 생성 완료 (개수: {len(my_list)})")

with open('sort_data.pkl', 'wb') as f:
    pickle.dump(my_list, f)