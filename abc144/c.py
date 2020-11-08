import math

n = int(input())
ans = 10**13

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        ans = min(ans, n // i + i - 2)
print(ans)