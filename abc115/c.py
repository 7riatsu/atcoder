n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]

arr.sort()

ans = arr[k - 1] - arr[0]

for i in range(0, len(arr) - k + 1):
    ans = min(ans, arr[i + k - 1] - arr[i])

print(ans)