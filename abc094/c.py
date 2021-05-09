n = int(input())
a = list(map(int, input().split()))

s_a = sorted(a)

l, r = s_a[len(s_a) // 2 - 1], s_a[len(s_a) // 2]

if l == r:
    for _ in a:
        print(l)
    exit()

for ele in a:
    if ele <= l:
        print(r)
    else:
        print(l)
