s = input()

cor = True

for char in s:
    if char == 'N':
        cor = "S" in s
    elif char == 'E':
        cor = "W" in s
    elif char == 'S':
        cor = "N" in s
    elif char == 'W':
        cor = "E" in s
    else:
        pass

    if not cor:
        break

if cor:
    print("Yes")
else:
    print("No")
