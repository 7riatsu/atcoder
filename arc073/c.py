n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(len(arr) - 1):
    ans += min(arr[i + 1] - arr[i], t)

ans += t
print(ans)