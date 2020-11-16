n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i, ele in enumerate(arr):
    if arr[ele - 1] == i + 1:
        cnt += 1
print(cnt // 2)