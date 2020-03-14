N = int(input())
d = dict()
ans = 0
for i in range(1, N + 1):
    if not (str(i)[0], str(i)[-1]) in d:
        d[(str(i)[0], str(i)[-1])] = 1
    else:
        d[(str(i)[0], str(i)[-1])] += 1
for j in d:
    if (j[-1], j[0]) in d:
        ans += d[j] * d[(j[-1], j[0])]
print(ans)