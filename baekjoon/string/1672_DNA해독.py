import sys
n = int(sys.stdin.readline().rstrip())
dna = list(sys.stdin.readline().rstrip())
trans = {"AG": "C", "AC": "A", "AT": "G", "GC": "T", "GT": "A", "CT": "G", "GA": "C", "CA": "A", "TA": "G", "CG": "T","TG": "A", "TC": "G"}
a = ""
b = dna.pop()
for _ in range(n - 1):
    a = dna.pop()
    if a == b:
        continue
    b = trans[a + b]
print(b)