s = input()
l = len(s)

ans = l * (l - 1)

for i in range(l):
    if s[i] == "U":
        ans += len(s[:i])
    else:
        ans += len(s[i + 1:])

print(ans)
