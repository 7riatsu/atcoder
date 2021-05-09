L, R = map(int, input().split())

if R - L >= 2019:
    print(0)
    exit()

ans = 2019
for l in range(L, R):
    for r in range(l+1, R+1):
        ans = min(ans, (l * r) % 2019)

print(ans)