w, h, x, y = map(int, input().split())

print(w * h / 2, int(w == x + x and h == y + y))
