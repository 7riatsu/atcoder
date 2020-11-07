n = int(input())
arr = list(map(int, input().split()))

l = len(arr)
ans = 0

arr.sort(reverse=True)
for i, ele in enumerate(arr):
    if (i + 1) % 2 == 0 and i <= (3 * n - 1) - n:
        ans += ele
print(ans)