q, h, s, d = map(int, input().split())
n = int(input())

s = min(s, 2 * (min(h, q * 2)))
d = min(d, 2 * s)

ans = n // 2 * d + n % 2 * s

print(ans)