n, l = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(input())

ans = ''

for ele in sorted(arr):
    ans += ele
print(ans)