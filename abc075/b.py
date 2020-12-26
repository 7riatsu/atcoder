h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]

# position list
pos_l = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

for i, line in enumerate(arr):
    for j, ele in enumerate(line):
        if arr[i][j] == '#':
            pass
        else:
            cnt = 0
            for pos in pos_l:
                if 0 <= pos[0] + i < h and 0 <= pos[1] + j < w:
                    if arr[i + pos[0]][j + pos[1]] == '#':
                        cnt += 1
            arr[i][j] = str(cnt)

for line in arr:
    print(''.join(line))