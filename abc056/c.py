x = int(input())

ans = 0

tmp = 0
while True:
    ans += 1
    tmp += ans
    if tmp >= x:
        break

print(ans)
