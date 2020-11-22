n = int(input())
arr = [int(input()) for i in range(n)]

cnt = 1
result = False
pushed = arr[0]

while cnt <= n:
    if pushed == 2:
        result = True
        break
    pushed = arr[pushed - 1]
    cnt += 1

if result:
    print(cnt)
else:
    print(-1)