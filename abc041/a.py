n, a, b = map(int, input().split())

if a > b:
    a, b = b, a

ans = 0
if abs(a - b) % 2 == 1:
    ans = min(a - 1, n - b) + 1 + (b - a - 1) // 2
else:
    ans = (b - a) // 2
print(ans)