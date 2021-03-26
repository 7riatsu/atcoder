import math

N = int(input())
L = list(map(int, input().split()))

dct = {}
for i in L:
    if i not in dct:
        dct[i] = 0
    dct[i] += 1

res = 0
for v in dct.values():
    res += math.comb(v, 2)

for i in L:
    print(res - dct[i] + 1)
