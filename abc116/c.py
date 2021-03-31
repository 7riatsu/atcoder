n = int(input())
h = [0] + list(map(int, input().split()))

ans = 0

for i in range(1, n + 1):
    ans += max(0, h[i] - h[i - 1])
print(ans)
