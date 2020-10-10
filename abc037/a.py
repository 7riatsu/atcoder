s = input()

a = ""
b = ""
ans = 0

for char in s:
    a += char
    if a != b:
        b = a
        a = ""
        ans += 1
print(ans)