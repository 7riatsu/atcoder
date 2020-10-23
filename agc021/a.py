n = list(map(int, input()))
c = n[0]

ans = 0
for i in range(len(n)):
    ans += n[i]

print(max(ans, c + 9 * (len(n) - 1) - 1))
