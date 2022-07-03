import sys
import re
input = sys.stdin.readline
data = input().rstrip()[6:-7]
data = re.sub(r'<div title="([\w ]*)">', 'title : \\1\n', data)
data = re.sub(r'</p>', '\n', data)
data = re.sub(r'</div>', '', data)
data = re.sub(r'<p>', '>', data)
data = re.sub(r'</?[\w ]*>', '', data)
data = re.sub(r' *\n *>', '\n>', data)
data = data.rstrip().split('\n')
for idx, i in enumerate(data):
    if i[0] == '>':
        data[idx] = re.sub(r' {2,}', ' ', i)
        data[idx] = re.sub(r'^>', '', data[idx])
print('\n'.join(data))
