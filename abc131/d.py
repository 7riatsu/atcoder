n = int(input())

a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x: x[1])

cur = 0
for ele in a:
    cur += ele[0]
    if cur <= ele[1]:
        continue
    else:
        print("No")
        exit()

print("Yes")
