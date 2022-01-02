x, y, w, h = map(int, input().split())
print(min([(h - y if h // 2 < y else y), (w - x if w // 2 < x else x)]))