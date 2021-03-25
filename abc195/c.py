n = int(input())

ans = 0

for i in range(3, 20, 3):
    if n >= 10 ** i:
        ans += n - (10 ** i - 1)

print(ans)