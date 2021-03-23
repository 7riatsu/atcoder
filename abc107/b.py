h, w = map(int, input().split())

lines = [list(map(str, input())) for _ in range(h)]
row = [True] * h
col = [True] * w

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            row[i] = False
            col[j] = False

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if not row[i]:
            if not col[j]:
                print(char, end="")
    print()
