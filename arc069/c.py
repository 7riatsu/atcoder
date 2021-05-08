n, m = map(int, input().split())

ans = 0

if 2 * n >= m:
    print(m // 2)
    exit()

m -= 2 * n

ans = n + (m // 4)
print(ans)
