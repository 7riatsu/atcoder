n, k = map(int, input().split())

def prob(roll: int) -> float:
    cnt = 0
    while roll < k:
        roll *= 2
        cnt += 1
    return (1 / n) * (1 / 2) ** cnt

ans = 0
for i in range(1, n + 1):
    ans += prob(i)
print(ans)
