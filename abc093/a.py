arr = sorted(list(map(int, input().split())))

a = arr[2] - arr[0]
b = arr[2] - arr[1]

tmp = max(a, b) - min(a, b)

if tmp % 2 == 1:
    ans = min(a, b) + (tmp + 1) // 2 + 1
else:
    ans = min(a, b) + tmp // 2

print(int(ans))
