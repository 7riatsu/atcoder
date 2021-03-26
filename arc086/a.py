n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = [0] * (n + 1)

for num in arr:
    tmp[num] += 1

tmp = sorted(tmp)
ans = cnt = 0

for num in reversed(tmp):
    cnt += 1
    if cnt <= k:
        pass
    elif cnt > k and num != 0:
        ans += num

print(ans)
