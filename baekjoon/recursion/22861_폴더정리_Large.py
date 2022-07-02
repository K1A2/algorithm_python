import sys
from collections import deque
from dataclasses import dataclass
from typing import List

@dataclass
class File:
    name: str

@dataclass
class Folder:
    name: str
    children_file: List['File']
    children_folder: List['Folder']

def get_target_foler(path):
    current = root
    idx = 1
    while len(path) > idx:
        for i in current.children_folder:
            if i.name == path[idx]:
                current = i
                idx += 1
                break
    return current

def count_files(target, all, files_count, files):
    for i in target.children_file:
        files.add(i.name)
        all += 1
    for i in target.children_folder:
        files_count, all = count_files(i, all, files_count, files)
    return len(files), all

def move(from_folder, to_folder):
    files_name = set([i.name for i in to_folder.children_file])
    for f in from_folder.children_file:
        if f.name not in files_name:
            to_folder.children_file.append(f)
            files_name.add(f.name)
    for f in from_folder.children_folder:
        to_folder.children_folder.append(f)

root = Folder(name='main', children_folder=[], children_file=[])
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
folders = dict()
folders['main'] = root

for _ in range(n + m):
    p, f, c = input().rstrip().split()
    if int(c):
        if p in folders and f in folders:
            folders[p].children_folder.append(folders[f])
        elif p in folders and f not in folders:
            folder = Folder(name=f, children_folder=[], children_file=[])
            folders[p].children_folder.append(folder)
            folders[f] = folder
        elif p not in folders and f in folders:
            parent = Folder(name=p, children_folder=[], children_file=[])
            parent.children_folder.append(folders[f])
            folders[p] = parent
        else:
            parent = Folder(name=p, children_folder=[], children_file=[])
            folder = Folder(name=f, children_folder=[], children_file=[])
            parent.children_folder.append(folder)
            folders[f] = folder
            folders[p] = parent
    else:
        if p in folders:
            file = File(name=f)
            folders[p].children_file.append(file)
        else:
            file = File(name=f)
            parent = Folder(name=p, children_folder=[], children_file=[])
            parent.children_file.append(file)
            folders[p] = parent

for _ in range(int(input().rstrip())):
    from_path, to_path = map(lambda x: x.split('/'), input().rstrip().split())
    from_folder = get_target_foler(from_path)
    to_folder = get_target_foler(to_path)
    move(from_folder, to_folder)

    from_folder_parent = get_target_foler(from_path[:-1])
    for idx, i in enumerate(from_folder_parent.children_folder):
        if i.name == from_folder.name:
            del from_folder_parent.children_folder[idx]
            break

for _ in range(int(input().rstrip())):
    print(*count_files(get_target_foler(input().rstrip().split('/')), 0, 0, set()))
