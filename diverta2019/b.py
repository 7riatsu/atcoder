r, g, b, n = map(int, input().split())
ans = 0

for i in range(3000 // r + 1):
    for j in range(3000 // g + 1):
        v = i * r + g * j
        if n >= v and (n - v) % b == 0:
            ans += 1
print(ans)
