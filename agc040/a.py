s = input()
ans = []

for i in range(len(s) + 1):
    l = r = 0
    l_str = s[:i]
    r_str = s[i:]

    for char in reversed(l_str):
        if char == "<":
            l += 1
        else:
            break

    for char in r_str:
        if char == ">":
            r += 1
        else:
            break
    ans.append(max(l, r))

print(sum(ans))
