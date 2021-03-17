n = int(input())
dp = [[0 for i in range(3)]]
l = [None]
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(1, n + 1):
    dpa = max(dp[-1][1], dp[-1][2]) + l[i][0]
    dpb = max(dp[-1][0], dp[-1][2]) + l[i][1]
    dpc = max(dp[-1][0], dp[-1][1]) + l[i][2]
    dp.append([dpa, dpb, dpc])
print(max(dp[-1]))