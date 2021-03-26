n = int(input())
s = input()
t = input()

ans = ""

for i in range(n):
    for j in range(n):
        if t[i] == s[j] and i == 0:
            if s[j:] == t[i:i + len(s[j:])]:
                ans = s[:j] + t
                break
if ans == "":
    ans = s + t
print(len(ans))