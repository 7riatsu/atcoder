import math

N, X = map(int, input().split())
arr = list(map(int, input().split()))

diff = [abs(X - num) for num in arr]

if len(diff) >= 2:
    ans = math.gcd(diff[0], diff[1])
    for i in range(1, len(diff)):
        ans = math.gcd(ans, diff[i])
else:
    ans = diff[0]
print(ans)
