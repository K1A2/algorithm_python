import sys
input = sys.stdin.readline
n = int(input().rstrip())
tree = [0 for _ in range(n)]
int_A = ord('A')
for _ in range(n):
    a, b, c = map(lambda x: ord(x) - int_A, input().rstrip().split())
    tree[a] = (b, c)

def preorder(i):
    print(chr(i + int_A), end='')
    if tree[i][0] >= 0: preorder(tree[i][0])
    if tree[i][1] >= 0: preorder(tree[i][1])
def inorder(i):
    if tree[i][0] >= 0: inorder(tree[i][0])
    print(chr(i + int_A), end='')
    if tree[i][1] >= 0: inorder(tree[i][1])
def postorder(i):
    if tree[i][0] >= 0: postorder(tree[i][0])
    if tree[i][1] >= 0: postorder(tree[i][1])
    print(chr(i + int_A), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)