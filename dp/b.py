n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [10 ** 9 for i in range(n)]
dp[0] = 0

for i in range(1, n):
    for j in range(k + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))
print(dp[-1])