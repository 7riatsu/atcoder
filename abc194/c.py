n = int(input())
arr = list(map(int, input().split()))

ans = 0
a = [0] * 401

for num in arr:
    a[num + 200] += 1

for i in range(len(a)):
    for j in range(i, len(a)):
        ans += a[i] * a[j] * ((i - j) ** 2)
print(ans)