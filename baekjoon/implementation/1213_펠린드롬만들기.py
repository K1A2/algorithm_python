from collections import deque

count = [0] * 26
input_s = list(input())
for s in input_s:
    count[ord(s) - ord('A')] += 1
odd_count = 0
odd_idx = -1
for idx, c in enumerate(count):
    if len(input_s) % 2 == 0 and c % 2 != 0:
        print("I'm Sorry Hansoo")
        exit()
    if c % 2 == 1:
        odd_count += 1
        odd_idx = idx
        if odd_count > 1:
            print("I'm Sorry Hansoo")
            exit()
d = deque()
if odd_idx >= 0:
    d.append(chr(odd_idx + ord('A')))
    count[odd_idx] -= 1

idx = 25
while idx >= 0:
    if count[idx] > 1:
        d.appendleft(chr(idx + ord('A')))
        d.append(chr(idx + ord('A')))
        count[idx] -= 2
    else:
        idx -= 1
print(''.join(d))
