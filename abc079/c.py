import itertools

s = input()
ans = ''

for i in ["-", "+"]:
    for j in ["-", "+"]:
        for k in ["-", "+"]:
            tmp = s[0] + i + s[1] + j + s[2] + k + s[3]
            if eval(tmp) == 7:
                ans = tmp + '=7'
print(ans)