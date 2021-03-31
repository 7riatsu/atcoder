s = input()
ans = ""

for char in s:
    if char == "0" or char == "1":
        ans += char
    elif char == "B":
        ans = ans[:-1]
    else:
        pass

print(ans)
