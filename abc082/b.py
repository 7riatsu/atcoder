s, t = input(), input()

s = "".join(sorted(s))
t = "".join(reversed(sorted(t)))

print("Yes" if s < t else "No")