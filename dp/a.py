n = int(input())
h_l = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    if i == 1:
        dp[i] = abs(h_l[i] - h_l[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(h_l[i] - h_l[i - 1]), dp[i - 2] + abs(h_l[i] - h_l[i - 2]))
print(dp[-1])