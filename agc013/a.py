n = int(input())
arr = list(map(int, input().split()))

status = "init"
ans = 0

for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        if status == "init":
            status = "plus"
        elif status == "plus":
            pass
        else:
            # statusを初期化
            status = "init"
            ans += 1
    elif arr[i] > arr[i + 1]:
        if status == "init":
            status = "minus"
        elif status == "minus":
            pass
        else:
            # statusを初期化
            status = "init"
            ans += 1
    else:
        pass
ans += 1

print(ans)