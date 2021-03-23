n = int(input())
arr = list(map(int, input().split()))

forward = [0] * n
back = [0] * n

for k, v in enumerate(arr):
    if k == 0:
        forward[k] = arr[k]
        back[k] = sum(arr)
    else:
        forward[k] = forward[k - 1] + v
        back[k] = back[k - 1] - arr[k - 1]

ans = 2020202020

for i in range(len(forward) - 1):
    ans = min(ans, abs(forward[i] - back[i + 1]))

print(ans)
