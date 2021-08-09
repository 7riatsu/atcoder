def gen_identifier(l, r):
    z = "000000"
    a = z + str(l)
    b = z + str(r)
    return a[len(a) - 6:len(a)] + b[len(b) - 6:len(b)]

n, m = map(int, input().split())
arr = []
d = {}
for i in range(m):
    x, y = map(int, input().split())
    arr.append([x, y])
    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]

for k, v in d.items():
    tmp = {v: k + 1 for k, v in enumerate(sorted(v))}
    d[k] = tmp

for ele in arr:
    x, y = ele[0], ele[1]
    y_pos = d[x][y]
    print(gen_identifier(x, y_pos))
