h, w = map(int, input().split())

lines = [list(map(str, input())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if lines[i][j] == "#":
            if i - 1 >= 0 and lines[i - 1][j] == "#" \
            or i + 1 < w and lines[i + 1][j] == "#" \
            or j - 1 >= 0 and lines[i][j - 1] == "#" \
            or j + 1 < h and lines[i][j + 1] == "#":
                continue
            else:
                print("No")
                exit()

print("Yes")
