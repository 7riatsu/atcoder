n = int(input())
a = list(map(int, input().split()))

d = {}
for ele in a:
    if ele in d:
        d[ele] += 1
    else:
        d[ele] = 1

tmp = [k for k, v in d.items() if v >= 2]
tmp2 = [k for k, v in d.items() if v >= 4]
tmp.sort()
tmp2.sort()

ans = 0
if len(tmp) >= 2:
    ans = tmp[-1] * tmp[-2]
if len(tmp2) >= 1:
    ans = max(ans, tmp2[-1] * tmp2[-1])

print(ans)


# a.sort()
# a.reverse()

# status, w, h = 0, 0, 0

# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         if status == 0:
#             w = a[i]
#             status = 1
#         elif status == 1 and a[i] != w:
#             h = a[i]

#             break

# print(w * h)