n = int(input())
arr = list(map(int, input().split()))

ans = True
mx = 0

for i in range(n):
    if arr[i] >= mx - 1:
        pass
    else:
        ans = False
        break
    mx = max(arr[i], mx)

if ans:
    print('Yes')
else:
    print('No')