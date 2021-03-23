s = input()
l_s = len(s)

ans = "keyence"
l_a = len(ans)

rm_num = l_s - l_a

for i in range(0, l_s - rm_num):
    if s[0:i] + s[rm_num + i :l_s] == ans:
        print("YES")
        exit()
print("NO")
