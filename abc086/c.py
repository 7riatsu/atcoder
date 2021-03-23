n = int(input())
curr = (0, 0, 0)

ans = True

for _ in range(n):
    t, x, y = map(int, input().split())
    diff = abs(curr[1] - x) + abs(curr[2] - y)
    if t - curr[0] >= diff and (t - curr[0] - diff) % 2 == 0:
        curr = (t, x, y)
        continue
    else:
        ans = False
        break

print("Yes" if ans else "No")
