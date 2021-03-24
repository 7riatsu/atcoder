n = int(input())
arr = [int(input()) for i in range(n)]
d = {}

for num in arr:
    if num in d.keys():
        d[num] += 1
    else:
        d[num] = 1

ans = 0
for k, v in d.items():
    if v % 2 == 0:
        pass
    else:
        ans += 1

print(ans)
