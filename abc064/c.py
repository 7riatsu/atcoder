N = int(input())
A = list(map(int, input().split()))

A.sort()

D = {
    'gray': [range(1, 400), 0],
    'brown': [range(400, 800), 0],
    'green': [range(800, 1200), 0],
    'light-blue': [range(1200, 1600), 0],
    'blue': [range(1600, 2000), 0],
    'yellow': [range(2000, 2400), 0],
    'orange': [range(2400, 2800), 0],
    'red': [range(2800, 3200), 0]
}

max_v = min_v = 0

for rate in A:
    if rate >= 3200:
        is_first_color = True
        color = ""
        for k, v in D.items():
            if v[1] != 0:
                is_first_color = False
                color = k
                continue
            else:
                color = k
        if is_first_color:
            D[color][1] += 1
        else:
            D[color][1] += 1
            max_v += 1
        continue

    for k, v in D.items():
        if rate in v[0] and v[1] == 0:
            max_v += 1
            min_v += 1
            v[1] += 1

print(*(min_v, max_v))