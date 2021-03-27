def check(arr, tar_i) -> int:
    l = list(reversed(arr[: tar_i]))
    r = arr[tar_i + 1 :]

    l_cnt = r_cnt = 0
    for ele in l:
        if ele == ".":
            l_cnt += 1
        else:
            break

    for ele in r:
        if ele == ".":
            r_cnt += 1
        else:
            break
    return l_cnt + r_cnt

h, w, x, y = map(int, input().split())
x -= 1
y -= 1

row = col = []
for i in range(h):
    s = input()
    if i == x:
        row = list(s)
    col.append(s[y])

ans = 1
ans += check(row, y) + check(col, x)
print(ans)
