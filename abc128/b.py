from operator import itemgetter, attrgetter

n = int(input())

arr = []

for i in range(n):
    i += 1
    s, p = map(str, input().split())
    p = int(p) * -1
    arr.append((s, p, i))

# print(sorted(arr, key=lambda student: student[1]))
arr = sorted(arr, key=itemgetter(0, 1))
for ele in arr:
    print(ele[2])