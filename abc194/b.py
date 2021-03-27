n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n):
    a[i], b[i] = map(int, input().split())

ans = 10e5 ** 2

for i in range(n):
    for j in range(n):
        ans = min(ans, a[i] + b[j] if i == j else max(a[i], b[j]))

print(ans)
